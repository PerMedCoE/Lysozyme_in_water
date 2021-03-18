from permedcoe import Container
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER


@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@Binary(binary='gmx')
@Task(structure_newbox=FILE_IN,
      protein_solv=FILE_OUT,
      topology=FILE_IN)
def add_solvate(mode='solvate',
                structure_newbox_flag='-cp', structure_newbox=None,
                configuration_solvent_flag='-cs', configuration_solvent='spc216.gro',
                protein_solv_flag='-o', protein_solv=None,
                topology_flag='-p', topology=None):
    # Command: gmx solvate -cp structure_newbox.gro -cs spc216.gro -o protein_solv.gro -p topology.top
    pass


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (str): Input file path.
        output (str): Output directory path.
        config (dict): Configuration dictionary.
    Returns:
        None
    """
    structure_newbox, topology = input
    protein_solv = output
    add_solvate(structure_newbox=structure_newbox,
                protein_solv=protein_solv,
                topology=topology)
