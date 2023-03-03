import os

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import Type, StdIOStream, STDIN


# Import container definition
from energy_analysis_BB.definitions import ENERGY_ANALYSIS_CONTAINER


@container(engine="SINGULARITY", image=ENERGY_ANALYSIS_CONTAINER)
@binary(binary='gmx')
@task(em=FILE_IN,
      output=FILE_OUT,
      selection={Type:FILE_IN, StdIOStream:STDIN})
def energy_analysis(mode='energy',
                    em_flag='-f', em=None,
                    output_flag='-o', output=None,
                    selection=None):
    # Command: gmx energy -f em.edr -o output.xvg
    pass



def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    em_energy = arguments.em_energy
    energy_selection = arguments.energy_selection
    energy_result = arguments.energy_result
    energy_analysis(em=em_energy,
                    output=energy_result,
                    selection=energy_selection)


