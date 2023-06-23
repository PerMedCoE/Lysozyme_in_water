#!/usr/bin/python3

"""
Lysozyme in Water - PyCOMPSs using PerMedCoE Building Blocks

This example will guide a new user through the process of setting up a
simulation system containing a set of proteins (lysozymes) in boxes of water,
with ions. Each step will contain an explanation of input and output,
using typical settings for general use.

Extracted from: http://www.mdtutorials.com/gmx/lysozyme/index.html
Originally done by: Justin A. Lemkul, Ph.D.
From: Virginia Tech Department of Biochemistry

This example reaches up to stage 4 (energy minimization).
"""

import sys
import time
from os import listdir
from os.path import isfile, join

# To set building block debug mode
from permedcoe import set_debug
# Import building block entry points
from add_solvate_BB import add_solvate
from assemble_tpr_BB import assemble_tpr
from define_box_BB import define_box
from energy_analysis_BB import energy_analysis
from energy_minimization_BB import energy_minimization
from generate_topology_BB import generate_topology, adapt_itp, clean_itps
from replace_solvent_with_ions_BB import replace_solvent_with_ions
from equilibrate_BB import equilibrate

# PyCOMPSs specific imports
from pycompss.api.api import compss_barrier


def main(dataset_path, output_path, config_path):
    print("Starting Lysozyme in Water")
    start_time = time.time()

    protein_names = []
    protein_pdbs = []

    # Look for proteins in the dataset folder
    for f in listdir(dataset_path):
        if isfile(join(dataset_path, f)):
            protein_names.append(f.split('.')[0])
            protein_pdbs.append(join(dataset_path, f))
    proteins = zip(protein_names, protein_pdbs)

    # Iterate over the proteins and process them
    for name, pdb in proteins:
        # 1st step - Generate topology
        structure = join(output_path, name + '.gro')
        topology = join(output_path, name + '.top')
        topology_itp = join(output_path, name + '_top.itp')
        generate_topology(protein=pdb,
                          structure=structure,
                          topology=topology,
                          topology_itp=topology_itp)
        adapt_itp(topology, topology_itp)
        # 2nd step - Define box
        structure_newbox = join(output_path, name + '_newbox.gro')
        define_box(structure=structure,
                   structure_newbox=structure_newbox)
        # 3rd step - Add solvate
        protein_solv = join(output_path, name + '_solv.gro')
        add_solvate(structure_newbox=structure_newbox,
                    protein_solv=protein_solv,
                    topology=topology)
        # 4th step - Add ions
        # Assemble with ions.mdp
        ions_conf = join(config_path, 'ions.mdp')
        ions = join(output_path, name + '_ions.tpr')
        assemble_tpr(conf=ions_conf,
                     protein_solv=protein_solv,
                     topology=topology,
                     output=ions)
        protein_solv_ions = join(output_path, name + '_solv_ions.gro')
        group = join(config_path, 'genion.group')
        replace_solvent_with_ions(ions=ions,
                                  output=protein_solv_ions,
                                  topology=topology,
                                  group=group)
        # 5th step - Minimize energy
        # Reasemble with minim.mdp
        minim_conf = join(config_path, 'minim.mdp')
        em = join(output_path, name + '_em.tpr')
        assemble_tpr(conf=minim_conf,
                     protein_solv=protein_solv_ions,
                     topology=topology,
                     output=em)
        em_energy = join(output_path, name + '_em.tpr')
        em_energy_structure = join(output_path, name + '_em.gro')
        em_energy_file = join(output_path, name + '_em.edr')
        em_energy_log = join(output_path, name + '_em.log')
        em_energy_trajectory = join(output_path, name + '_em.trr')
        energy_minimization(energy=em_energy,
                            structure=em_energy_structure,
                            file=em_energy_file,
                            log=em_energy_log,
                            trajectory=em_energy_trajectory,
                            steps="100")
        # 6th step - Energy analysis (generate xvg image)
        energy_result = join(output_path, name + '_potential.xvg')
        energy_selection = join(config_path, 'energy.selection')
        energy_analysis(em=em_energy_file,
                        output=energy_result,
                        selection=energy_selection)
        #################################################
        ################### SOLUTION ####################
        #################################################
        # 7th step - Equilibrate
        equilibrate_conf = join(config_path, 'nvt.mdp')
        equilibrate_output = join(output_path, name + '_nvt.tpr')
        equilibrate(conf=equilibrate_conf,
                    structure_file=em_energy_structure,
                    structure2_file=em_energy_structure,
                    topology=topology,
                    output=equilibrate_output)
        # Reuse energy minimization
        equilibrate_structure = join(output_path, name + '_eq.gro')
        equilibrate_file = join(output_path, name + '_eq.edr')
        equilibrate_log = join(output_path, name + '_eq.log')
        equilibrate_trajectory = join(output_path, name + '_eq.trr')
        energy_minimization(energy=equilibrate_output,
                            structure=equilibrate_structure,
                            file=equilibrate_file,
                            log=equilibrate_log,
                            trajectory=equilibrate_trajectory,
                            steps="100")
        # Analyse energy again (temperature)
        equilibrate_result = join(output_path, name + '_temperature.xvg')
        temperature_selection = join(config_path, 'temperature.selection')
        energy_analysis(em=equilibrate_file,
                        output=equilibrate_result,
                        selection=temperature_selection)

    #################################################
    # Cleanup
    compss_barrier()
    clean_itps()

    #################################################
    # Elapsed time
    elapsed_time = time.time() - start_time
    print("Elapsed time: %s" % str(elapsed_time))


if __name__=='__main__':
    dataset_path = sys.argv[1]
    output_path = sys.argv[2]
    config_path = sys.argv[3]

    main(dataset_path, output_path, config_path)
