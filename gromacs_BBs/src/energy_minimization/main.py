from permedcoe import container
# from permedcoe import constraint
# from permedcoe import mpi
from permedcoe import binary
from permedcoe import task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER

# computing_units = "24"
# computing_nodes = "1"

@container(engine="SINGULARITY", image=GROMACS_CONTAINER)
# @constraint(computing_units=computing_units)
# @mpi(runner="mpirun", binary="gmx_mpi", computing_nodes=computing_nodes)
@binary(binary='gmx')   # mpi candidate
@task(em=FILE_IN,
      em_energy=FILE_OUT)
def energy_minimization(mode='mdrun',
                        verbose_flag='-v',
                        ompthreads_flag='-ntomp', ompthreads='0',
                        em_flag='-s', em=None,
                        em_energy_flag='-e', em_energy=None):
    # Command: gmx mdrun -v -s em.tpr
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
    em = input
    em_energy = output
    energy_minimization(em=em,
                        em_energy=em_energy)
