import os
try:
    from permedcoe.bb import CONTAINER_PATH
    from permedcoe.bb import COMPUTING_UNITS
except Exception:
    CONTAINER_PATH = str(os.environ["HOME"]) + "/github/projects/PerMedCoE/Lysozyme_in_water/gromacs_BBs/image/"
    COMPUTING_UNITS = 1

# Do not change this line
BB_SOURCE_PATH=os.path.dirname(os.path.abspath(__file__))

# Update the following lines:
#  - Container definition for energy minimization Building Block
ENERGY_MINIMIZATION_CONTAINER = CONTAINER_PATH + "gromacs.sif"
