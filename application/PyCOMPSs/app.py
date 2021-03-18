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
from os import listdir
from os.path import isfile, join

# To set building block debug mode
from permedcoe import set_debug
# Import building block entry points
from add_solvate import add_solvate
from assemble_tpr import assemble_tpr
from define_box import define_box
from energy_analysis import energy_analysis
from energy_minimization import energy_minimization
from generate_topology import generate_topology
from replace_solvent_with_ions import replace_solvent_with_ions


def main(dataset_path, output_path, config_path):
    print("Starting Lysozyme in Water")

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
        generate_topology(protein=pdb,
                          structure=structure,
                          topology=topology)
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
        em_energy = join(output_path, name + '_em_energy.edr')
        energy_minimization(em=em,
                            em_energy=em_energy)
        # 6th step - Energy analysis (generate xvg image)
        energy_result = join(output_path, name + '_potential.xvg')
        energy_selection = join(config_path, 'energy.selection')
        energy_analysis(em=em_energy,
                        output=energy_result,
                        selection=energy_selection)


if __name__=='__main__':
    dataset_path = sys.argv[1]
    output_path = sys.argv[2]
    config_path = sys.argv[3]

    main(dataset_path, output_path, config_path)
