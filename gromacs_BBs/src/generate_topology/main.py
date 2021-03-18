from permedcoe import Container
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER


@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@Binary(binary='gmx')
@Task(protein=FILE_IN,
      structure=FILE_OUT,
      topology=FILE_OUT)
def generate_topology(mode='pdb2gmx',
                      protein_flag='-f', protein=None,
                      structure_flag='-o', structure=None,
                      topology_flag='-p', topology=None,
                      flags='-ignh',
                      forcefield_flag='-ff', forcefield='oplsaa',
                      water_flag='-water', water='spce'):
    # Command: gmx pdb2gmx -f protein.pdb -o structure.gro -p topology.top -ignh -ff amber03 -water tip3p
    pass


def invoke(input, output, config={}):
    """ Common interface.

    Args:
        input (str): Input file path.
        output (str): Output directory path.
        config (dict): Configuration dictionary.
    Returns:
        None
    """
    pdb = input
    structure, output = output
    generate_topology(protein=pdb,
                      structure=structure,
                      topology=output)
