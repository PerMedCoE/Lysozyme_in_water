from permedcoe import Container
from permedcoe import Binary
from permedcoe import Task

from permedcoe import FILE_IN
from permedcoe import FILE_OUT
from permedcoe import Type, StdIOStream, STDIN

# Import single container definition
from gromacs_BBs_commons.image import GROMACS_CONTAINER


@Container(engine="SINGULARITY", image=GROMACS_CONTAINER)
@Binary(binary='gmx')
@Task(em=FILE_IN,
      output=FILE_OUT,
      selection={Type:FILE_IN, StdIOStream:STDIN})
def energy_analysis(mode='energy',
                    em_flag='-f', em=None,
                    output_flag='-o', output=None,
                    selection=None):
    # Command: gmx energy -f em.edr -o output.xvg
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
    em_energy, energy_selection = input
    energy_result = output
    energy_analysis(em=em_energy,
                    output=energy_result,
                    selection=energy_selection)
