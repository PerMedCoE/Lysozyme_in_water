from permedcoe import container
from permedcoe import binary
from permedcoe import task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER


@container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@binary(binary='gmx')
@task(structure=FILE_IN,
      structure_newbox=FILE_OUT)
def define_box(mode='editconf',
               structure_flag='-f', structure=None,
               structure_newbox_flag='-o', structure_newbox=None,
               center_flag='-c',
               distance_flag='-d', distance='1.0',
               boxtype_flag='-bt', boxtype='cubic'):
    # Command: gmx editconf -f structure.gro -o structure_newbox.gro -c -d 1.0 -bt cubic
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
    define_box(structure=input,
               structure_newbox=output)
