from permedcoe import Container
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER


@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@Binary(binary='gmx')
@Task(conf=FILE_IN,
      protein_solv=FILE_IN,
      topology=FILE_IN,
      output=FILE_OUT)
def assemble_tpr(mode='grompp',
                 conf_flag='-f', conf=None,
                 protein_solv_flag='-c', protein_solv=None,
                 topology_flag='-p', topology=None,
                 output_flag='-o', output=None):
    # Command: gmx grompp -f ions.mdp -c protein_solv.gro -p topology.top -o ions.tpr
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
    ions_conf, protein_solv, topology = input
    group = output
    assemble_tpr(conf=ions_conf,
                 protein_solv=protein_solv,
                 topology=topology,
                 output=group)
