import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from assemble_tpr_BB.definitions import ASSEMBLE_TPR_CONTAINER


@container(engine="SINGULARITY", image=ASSEMBLE_TPR_CONTAINER)
@binary(binary='gmx')
@task(conf=FILE_IN,
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



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    ions_conf = arguments.ions_conf
    protein_solv = arguments.protein_solv
    topology = arguments.topology
    group = arguments.group
    assemble_tpr(conf=ions_conf,
                 protein_solv=protein_solv,
                 topology=topology,
                 output=group)

