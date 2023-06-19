import os
import fileinput
from shutil import copy2

from permedcoe import container
from permedcoe import binary
from permedcoe import task
from permedcoe import FILE_IN
from permedcoe import FILE_INOUT
from permedcoe import FILE_OUT

# Import container definition
from generate_topology_BB.definitions import GENERATE_TOPOLOGY_CONTAINER


SHARED_FOLDER = os.environ.get("HOME") + "/tmp/"
if not os.path.exists(SHARED_FOLDER):
    os.makedirs(SHARED_FOLDER)


@container(engine="SINGULARITY", image=GENERATE_TOPOLOGY_CONTAINER)
@binary(binary='gmx')
@task(protein=FILE_IN,
      structure=FILE_OUT,
      topology=FILE_OUT,
      topology_itp=FILE_OUT)
def generate_topology(mode='pdb2gmx',
                      protein_flag='-f', protein=None,
                      structure_flag='-o', structure=None,
                      topology_flag='-p', topology=None,
                      topology_itp_flag='-i', topology_itp=None,
                      flags='-ignh',
                      forcefield_flag='-ff', forcefield='oplsaa',
                      water_flag='-water', water='spce'):
    # Command: gmx pdb2gmx -f protein.pdb -o structure.gro -p topology.top -i posre.itp -ignh -ff amber03 -water tip3p
    pass


@task(topology=FILE_INOUT,
      topology_itp=FILE_IN)
def adapt_itp(topology, topology_itp):
    """
    Plain python task to adapt the itp path inside the topology file.

    Gromacs hardcodes the path of the itp file into the topology file.
    Since the files are copied to the sandbox, the hardcoded path includes the
    sandbox folder.
    Consequently, we need to place the itp files in a shared folder and modify
    the topology file to point to its corresponding itp file.

    WARNING: Requires shared folder where to place the topology_itp files.
    """
    # Copy itp file to a common shared place
    copy2(topology_itp, SHARED_FOLDER)
    # Look for:
    file_name = os.path.basename(topology_itp)
    shared_destination = SHARED_FOLDER + file_name
    # Update the itp path into the topology file
    for line in fileinput.input(topology, inplace=True):
        if file_name in line and "#include" in line:
            print("#include \"" + shared_destination + "\"\n", end='')
        else:
            print(line, end='')


def clean_itps():
    """
    Clean all itp files in the shared folder
    """
    for item in os.listdir(SHARED_FOLDER):
        if item.endswith(".itp"):
            os.remove(os.path.join(SHARED_FOLDER, item))


def invoke(arguments, config):
    """ Common interface.

    Args:
        arguments (args): Building Block parsed arguments.
        config (dict): Configuration dictionary (not used).
    Returns:
        None
    """
    pdb = arguments.pdb
    structure = arguments.structure
    topology = arguments.topology
    topology_itp = arguments.topology_itp
    generate_topology(protein=pdb,
                      structure=structure,
                      topology=topology,
                      topology_itp=topology_itp)


