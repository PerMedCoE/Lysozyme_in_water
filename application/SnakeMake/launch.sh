#!/bin/bash
#SBATCH --account=project_2007898
#SBATCH --partition=medium
#SBATCH --nodes=1
#SBATCH --time=00:15:00
mkdir -p out
snakemake -j 10 --config config_dir=../config dataset_dir=../dataset_small
