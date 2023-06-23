import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from equilibrate_BB.definitions import EQUILIBRATE_CONTAINER


@container(engine="SINGULARITY", image=EQUILIBRATE_CONTAINER)
@binary(binary="gmx")
@task(conf=FILE_IN,
      structure_file=FILE_IN,
      structure2_file=FILE_IN,
      topology=FILE_IN,
      output=FILE_OUT)
def equilibrate(mode="grompp",
                conf_flag="-f", conf=None,
                structure_file_flag="-c", structure_file=None,
                structure2_file_flag="-r", structure2_file=None,
                topology_flag="-p", topology=None,
                output_flag="-o", output=None):
    # Command: gmx grompp -f nvt.mdp -c em.gro -r em.gro -p topol.top -o nvt.tpr
    pass



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    conf = arguments.conf
    structure_file = arguments.structure_file
    structure2_file = arguments.structure2_file
    topology = arguments.topology
    result = arguments.result

    equilibrate(conf=conf,
                structure_file=structure_file,
                structure2_file=structure2_file,
                topology=topology,
                output=result)
