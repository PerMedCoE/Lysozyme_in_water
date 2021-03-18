from permedcoe import Container
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import Type, StdIOStream, STDIN

# Container definition for this building block
GROMACS_CONTAINER = "/home/javier/gitlab/projects/permedcoe/gromacs_BBs/image/gromacs.sif"


@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@Binary(binary='gmx')
@Task(ions=FILE_IN,
      output=FILE_OUT,
      topology=FILE_IN,
      group={Type:FILE_IN, StdIOStream:STDIN})
def replace_solvent_with_ions(mode='genion',
                              ions_flag='-s', ions=None,
                              output_flag='-o', output=None,
                              topology_flag='-p', topology=None,
                              pname_flag='-pname', pname='NA',
                              nname_flag='-nname', nname='CL',
                              neutral_flag='-neutral',
                              group=None):
    # Command: gmx genion -s ions.tpr -o 1AKI_solv_ions.gro -p topol.top -pname NA -nname CL -neutral < ../config/genion.group
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
    ions, topology, group = input
    protein_solv_ions = output
    replace_solvent_with_ions(ions=ions,
                              output=protein_solv_ions,
                              topology=topology,
                              group=group)
