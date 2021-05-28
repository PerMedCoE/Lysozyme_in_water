#!/usr/bin/python3

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT


# Define the path to the container
# SAMPLE_CONTAINER = "/path/to/image.sif"
# Or alternatively, import single container definition (it already has gromacs)
from gromacs_BBs_commons.image import GROMACS_CONTAINER as SAMPLE_CONTAINER


@container(engine="SINGULARITY", image=SAMPLE_CONTAINER)
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


def invoke(input, output, config):
    """ Common interface.

    Args:
        input (str): Input file path.
        output (str): Output directory path.
        config (dict): Configuration dictionary.
    Returns:
        None
    """
    conf = input[0]
    structure_file = input[1]
    structure2_file = input[2]
    topology = input[3]

    equilibrate(conf=conf,
                structure_file=structure_file,
                structure2_file=structure2_file,
                topology=topology,
                output=output)
