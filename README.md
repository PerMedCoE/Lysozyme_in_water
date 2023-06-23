# HPC/Exascale Centre of Excellence in Personalised Medicine

## Lysozyme in Water application

This repository contains the Lysozyme in Water sample application using a set of Building Blocks (BB) that internally use `gromacs` within the **HPC/Exascale Centre of Excellence in Personalised Medicine** ([PerMedCoE](https://permedcoe.eu/)) project.

This example guides users through the process of setting up a simulation system containing a set of proteins (lysozymes) in boxes of water, with ions.
Each step contain an explanation of input and output, using typical settings for general use.

Extracted from: <http://www.mdtutorials.com/gmx/lysozyme/index.html>

Originally done by: Justin A. Lemkul, Ph.D.

From: Virginia Tech Department of Biochemistry

> NOTE: This example reaches up to stage 4 (energy minimization).

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Lysozyme in Water application](#lysozyme-in-water-application)
  - [Table of Contents](#table-of-contents)
  - [Repository contents](#repository-contents)
  - [Requirements](#requirements)
  - [Usage](#usage)
    - [1st - Install `permedcoe` package](#1st---install-permedcoe-package)
    - [2th - Download the Lysozyme in water sources](#2th---download-the-lysozyme-in-water-sources)
    - [3th - Create the Singularity container](#3th---create-the-singularity-container)
    - [4th - Install the `gromacs_BBs` Building Blocks](#4th---install-the-gromacs_bbs-building-blocks)
    - [5th - Execute the `lysozyme_in_water` application](#5th---execute-the-lysozyme_in_water-application)
      - [5.1 **Bare**: Sequential implementation as a bash script using the building blocks directly.](#51-bare-sequential-implementation-as-a-bash-script-using-the-building-blocks-directly)
      - [5.2 **SnakeMake**: Parallelized with SnakeMake.](#52-snakemake-parallelized-with-snakemake)
      - [5.3 **PyCOMPSs**: Parallelized with PyCOMPSs.](#53-pycompss-parallelized-with-pycompss)
  - [License](#license)
  - [Contact](#contact)

## Repository contents

- **PerMedCoE:** PerMedCoE base package.
- **gromacs_BBs:** Set of building blocks using gromacs.
- **application:** Lysozyme in water application using the `gromacs_BBs`


## Requirements

- Python >= 3.6
- [Singularity](https://singularity.lbl.gov/docs-installation)
- [PyCOMPSs](https://pycompss.readthedocs.io/en/latest/Sections/00_Quickstart.html)
- (Optional: For results visualization) [Grace](https://plasma-gate.weizmann.ac.il/Grace/)

## Usage

### 1<sup>st</sup> - Install `permedcoe` package

  ``` bash
  python3 -m pip install permecoe
  ```

### 2<sup>th</sup> - Download the Lysozyme in water sources

  ``` bash
  git clone https://github.com/PerMedCoE/Lysozyme_in_water.git
  ```

### 3<sup>th</sup> - Create the Singularity container

  ``` bash
  cd Lysozyme_in_water/gromacs_BBs/image
  ./build.sh
  cd ..
  ```

### 4<sup>th</sup> - Install the `gromacs_BBs` Building Blocks

  ``` bash
  ./install_BBs.sh
  cd ..
  ```

### 5<sup>th</sup> - Execute the `lysozyme_in_water` application

There are three versions of the `lysozyme_in_water` application:

#### 5.1 **Bare**: Sequential implementation as a bash script using the building blocks directly.
  ``` bash
  cd application/Bare
  ./steps.sh
  # Check output folder (use "grace" to visualize xvg files).
  cd ../..
  ```

#### 5.2 **SnakeMake**: Parallelized with SnakeMake.
  ``` bash
  cd application/SnakeMake
  snakemake Snakefile
  # Check output folder (use "grace" to visualize xvg files).
  cd ../..
  ```

#### 5.3 **PyCOMPSs**: Parallelized with PyCOMPSs.

  ``` bash
  cd application/PyCOMPSs
  ./launch.sh
  # Check output folder (use "grace" to visualize xvg files).
  cd ../..
  ```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>

This software has been developed for the [PerMedCoE project](https://permedcoe.eu/), funded by the European Commission (EU H2020 [951773](https://cordis.europa.eu/project/id/951773)).

![](https://permedcoe.eu/wp-content/uploads/2020/11/logo_1.png "PerMedCoE")
