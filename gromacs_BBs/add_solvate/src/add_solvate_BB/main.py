import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from add_solvate_BB.definitions import ADD_SOLVATE_CONTAINER


@container(engine="SINGULARITY", image=ADD_SOLVATE_CONTAINER)
@binary(binary='gmx')
@task(structure_newbox=FILE_IN,
      protein_solv=FILE_OUT,
      topology=FILE_IN)
def add_solvate(mode='solvate',
                structure_newbox_flag='-cp', structure_newbox=None,
                configuration_solvent_flag='-cs', configuration_solvent='spc216.gro',
                protein_solv_flag='-o', protein_solv=None,
                topology_flag='-p', topology=None):
    # Command: gmx solvate -cp structure_newbox.gro -cs spc216.gro -o protein_solv.gro -p topology.top
    pass



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    structure_newbox = arguments.structure_newbox
    topology = arguments.topology
    protein_solv = arguments.protein_solv
    add_solvate(structure_newbox=structure_newbox,
                protein_solv=protein_solv,
                topology=topology)

