# HPC/Exascale Centre of Excellence in Personalised Medicine

## Lysozyme in Water application

This repository contains the Lysozyme in Water sample application using a set of Building Blocks (BB) that internally use `gromacs` within the **HPC/Exascale Centre of Excellence in Personalised Medicine** ([PerMedCoE](https://permedcoe.eu/)) project.

## Table of Contents

- [HPC/Exascale Centre of Excellence in Personalised Medicine](#hpcexascale-centre-of-excellence-in-personalised-medicine)
  - [Lysozyme in Water application](#lysozyme-in-water-application)
  - [Table of Contents](#table-of-contents)
  - [Repository contents](#repository-contents)
  - [Usage](#usage)
    - [1<sup>st</sup> - Install `permedcoe` package](#1supstsup---install-permedcoe-package)
    - [2<sup>th</sup> - Install the `gromacs_BBs` Building Blocks](#2supthsup---install-the-gromacs_bbs-building-blocks)
    - [3<sup>th</sup> - Execute the `lysozyme_in_water` application](#3supthsup---execute-the-lysozyme_in_water-application)
  - [License](#license)
  - [Contact](#contact)

## Repository contents

- **PerMedCoE:** PerMedCoE base package.
- **gromacs_BBs:** Set of building blocks using gromacs.
- **application:** Lysozyme in water application using the `gromacs_BBs`

## Usage

### 1<sup>st</sup> - Install `permedcoe` package

  ``` bash
  git clone https://github.com/PerMedCoE/permedcoe.git
  cd permedcoe
  ./install.sh
  cd ..
  ```

### 2<sup>th</sup> - Install the `gromacs_BBs` Building Blocks

  ``` bash
  git clone https://github.com/PerMedCoE/Lysozyme_in_water.git
  cd Lysozyme_in_water/gromacs_BBs
  ./install.sh
  cd ../..
  ```

### 3<sup>th</sup> - Execute the `lysozyme_in_water` application

  > NOTE: Requires PyCOMPSs installed in the machine.

  ``` bash
  cd Lysozyme_in_water/application/PyCOMPSs
  ./launch.sh
  # See output folder (use grace to visualize xvg files).
  cd ../../..
  ```

## License

[Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0)

## Contact

<https://permedcoe.eu/contact/>

