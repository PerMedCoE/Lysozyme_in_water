#!/usr/bin/env bash

export PERMEDCOE_IMAGES="$(pwd)/../../gromacs_BBs/image/"

# Explicit call with PyCOMPSs runcompss command:
runcompss -d -g --python_interpreter=python3 \
     app_complete.py \
     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/config

