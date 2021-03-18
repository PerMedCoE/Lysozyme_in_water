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
    - [1<sup>st</sup> - Install `permedcoe` package](#1supstsup---install-permedcoe-package)
    - [2<sup>th</sup> - Download the Lysozyme in water sources](#2supthsup---download-the-lysozyme-in-water-sources)
    - [3<sup>th</sup> - Create the Singularity container](#3supthsup---create-the-singularity-container)
    - [4<sup>nd</sup> - Set the Singularity image in the `gromacs_BBs` package](#4supndsup---set-the-singularity-image-in-the-gromacs_bbs-package)
    - [5<sup>th</sup> - Install the `gromacs_BBs` Building Blocks](#5supthsup---install-the-gromacs_bbs-building-blocks)
    - [6<sup>th</sup> - Execute the `lysozyme_in_water` application](#6supthsup---execute-the-lysozyme_in_water-application)
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
  git clone https://github.com/PerMedCoE/permedcoe.git
  cd permedcoe
  ./install.sh
  cd ..
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

### 4<sup>nd</sup> - Set the Singularity image in the `gromacs_BBs` package

  ```shell
  # Edit src/gromacs_BBs_commons/image.py
  # Set the SAMPLE_CONTAINER variable:
  #    It is currently set to: $HOME/github/projects/PerMedCoE/Lysozyme_in_water/gromacs_BBs/image/gromacs.sif
  #    And that path should be where the gromacs.sif file has been created in the previous step.
  ```

### 5<sup>th</sup> - Install the `gromacs_BBs` Building Blocks

  ``` bash
  ./install.sh
  cd ..
  ```

### 6<sup>th</sup> - Execute the `lysozyme_in_water` application

  ``` bash
  cd application/PyCOMPSs
  ./launch.sh
  # See output folder (use "grace" to visualize xvg files).
  cd ../..
  ```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>

