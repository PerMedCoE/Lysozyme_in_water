from permedcoe import Container
# from permedcoe import Constraint
# from permedcoe import Mpi
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Container definition for this building block
GROMACS_CONTAINER = "/home/javier/gitlab/projects/permedcoe/gromacs_BBs/image/gromacs.sif"

computing_units = "24"
computing_nodes = "1"

@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
# @Constraint(computing_units=computing_units)
# @Mpi(runner="mpirun", binary="gmx_mpi", computing_nodes=computing_nodes)
@Binary(binary='gmx')   # mpi candidate
@Task(em=FILE_IN,
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
