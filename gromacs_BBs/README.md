# HPC/Exascale Centre of Excellence in Personalised Medicine

## Gromacs Building Blocks

This package provides a set of **Building Blocks (BB)** for Gromacs using the **HPC/Exascale Centre of Excellence in Personalised Medicine** (
[PerMedCoE](https://permedcoe.eu/)) base Building Block.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Gromacs Building Blocks](#gromacs-building-blocks)
  - [Table of Contents](#table-of-contents)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [License](#license)
  - [Contact](#contact)

## User instructions

### Requirements

- Python >= 3.6
- Singularity

### Installation

There are two ways to install this package (from Pypi and manually):

- From Pypi:

  This package is NOT YET publicly available in Pypi:

  ```bash
  pip install gromacs_BB
  ```

  or more specifically:

  ```bash
  python3 -m pip install gromacs_BB
  ```

- From source code:

  This package provides an automatic installation script:

  ```bash
  ./install.sh
  ```

  This script creates a file `installation_files.txt` to keep track of the installed files. It is used with the `uninstall.sh` script to clean up the system.

### Usage

The `gromacs_BB` package provides a clear interface that allows it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and Snakemake).

- Command line interface:

  Once installed the `gromacs_BB` package, it provides the:

  - `add_solvate`
  - `assemble_tpr`
  - `define_box`
  - `energy_analysis`
  - `energy_minimization`
  - `generate_topology`
  - `replace_solvent_with_ions`

  commands, that can be used from the command line. For example:

  ```text
  $ generate_topology -h
  usage: generate_topology [-h] [-d] [-l {debug,info,warning,error,critical}] [--tmpdir TMPDIR]
                          [--processes PROCESSES] [--gpus GPUS] [--memory MEMORY]
                          [--mount_points MOUNT_POINTS]
                          input output config

  positional arguments:
    input                 Input file or directory path
    output                Output file or directory path
    config                Configuration file path

  optional arguments:
    -h, --help            show this help message and exit
    -d, --debug           Enable Building Block debug mode. Overrides log_level
    -l {debug,info,warning,error,critical}, --log_level {debug,info,warning,error,critical}
                          Set logging level
    --tmpdir TMPDIR       Temp directory to be mounted in the container
    --processes PROCESSES
                          Number of processes for MPI executions
    --gpus GPUS           Requirements for GPU jobs
    --memory MEMORY       Memory requirement
    --mount_points MOUNT_POINTS
                          Comma separated alias:folder to be mounted in the container
  ```

  This interface can be used within any workflow manager that requires binaries (e.g. NextFlow and Snakemake).

  In addition, any building block requires to have a function being called from the `__main__`, so that it can also be invoked from Python scripts. This allows to use the BB from PyCOMPSs seamlessly.

  ```python
  from generate_topology import invoke

  invoke(input, output, config)
  ```

- Extension for PyCOMPSs:

    Moreover, a BB can also implement a Python function not limited to the input (file or directory), output (file or directory) and config (yaml file) signature. This enables application developers to use the BB with PyCOMPSs using Python objects instead of files among BBs.

    ```python
    from generate_topology import generate_topology

    @Task(protein=FILE_IN,
          structure=FILE_OUT,
          topology=FILE_OUT)
    def generate_topology(mode='pdb2gmx',
                          protein_flag='-f', protein=None,
                          structure_flag='-o', structure=None,
                          topology_flag='-p', topology=None,
                          flags='-ignh',
                          forcefield_flag='-ff', forcefield='oplsaa',
                          water_flag='-water', water='spce'):
    ```

### Uninstall

Uninstall can be done as usual `pip` packages:

```bash
pip uninstall gromacs_BB
```

or more specifically:

```bash
./uninstall.sh
./clean.sh
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>
