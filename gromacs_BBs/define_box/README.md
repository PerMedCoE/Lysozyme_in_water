# Define Box Building Block

This package provides the define box **Building Block (BB)**.

## Table of Contents

- [Define Box Building Block](#define-box-building-block)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [User instructions](#user-instructions)
    - [Requirements](#requirements)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Uninstall](#uninstall)
  - [License](#license)
  - [Contact](#contact)

## Description

This is the define box building block.

## User instructions

### Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- `permedcoe` base package: `python3 -m pip install permedcoe`


### Installation

This package provides an automatic installation script:

```bash
./install.sh
```

### Usage

The `define_box_BB` package provides a clear interface that allows
it to be used with multiple workflow managers (e.g. PyCOMPSs, NextFlow and
Snakemake).

It can be imported from python and invoked directly from a **PyCOMPSs**
application, or through the command line for other workflow managers
(e.g. Snakemake and NextFlow).

The command line is:

```bash
define_box_BB -d \
    --structure_newbox <STRUCTURE_NEWBOX>
    --topology <TOPOLOGY>
    --protein_solv <PROTEIN_SOLV>
```

Where the parameters are:

|        | Flag               | Parameter           | Type | Description             |
|--------|--------------------|---------------------|------|-------------------------|
| Input  | --structure_newbox | \<STRUCTURE_NEWBOX> | File | Structure new box file. |
| Input  | --topology         | \<TOPOLOGY>         | File | Topology file.          |
| Output | --protein_solv     | \<PROTEIN_SOLV>     | File | Protein solvate.        |


### Uninstall

Uninstall can be achieved by executing the following scripts:

```bash
./uninstall.sh
./clean.sh
```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
