import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import Type, StdIOStream, STDIN

# Import container definition
from replace_solvent_with_ions_BB.definitions import REPLACE_SOLVENT_WITH_IONS_CONTAINER


@container(engine="SINGULARITY", image=REPLACE_SOLVENT_WITH_IONS_CONTAINER)
@binary(binary='gmx')
@task(ions=FILE_IN,
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



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    ions = arguments.ions
    topology = arguments.topology
    group = arguments.group
    protein_solv_ions = arguments.protein_solv_ions
    replace_solvent_with_ions(ions=ions,
                              output=protein_solv_ions,
                              topology=topology,
                              group=group)

