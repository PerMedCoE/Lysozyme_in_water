import os

from permedcoe import container
# from permedcoe import constraint
# from permedcoe import mpi
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT

# Import container definition
from energy_minimization_BB.definitions import ENERGY_MINIMIZATION_CONTAINER

# computing_units = "24"
# computing_nodes = "1"


@container(engine="SINGULARITY", image=ENERGY_MINIMIZATION_CONTAINER)
# @constraint(computing_units=computing_units)
# @mpi(runner="mpirun", binary="gmx_mpi", computing_nodes=computing_nodes)
@binary(binary='gmx')   # mpi candidate
@task(energy=FILE_IN,
      structure=FILE_OUT,
      file=FILE_OUT,
      log=FILE_OUT,
      trajectory=FILE_OUT)
def energy_minimization(mode='mdrun',
                        ompthreads_flag='-ntomp', ompthreads='0',
                        em_energy_flag='-s', energy=None,
                        em_energy_structure_flag='-c', structure=None,
                        em_energy_file_flag='-e', file=None,
                        em_energy_log_flag='-g', log=None,
                        em_energy_trajectory_flag='-o', trajectory=None,
                        steps_flags='-nsteps', steps='-2'):
    # Command: gmx mdrun -v -ntomp 0 -s 1aki_em.tpr -c 1aki_em.gro -e 1aki_em.edr -g 1aki_md.log -o 1aki_traj.trr
    pass



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    energy = arguments.energy
    structure = arguments.structure
    filename = arguments.filename
    log = arguments.log
    trajectory = arguments.trajectory
    energy_minimization(energy=energy,
                        structure=structure,
                        file=filename,
                        log=log,
                        trajectory=trajectory)

