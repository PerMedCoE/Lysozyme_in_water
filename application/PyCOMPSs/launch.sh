#!/usr/bin/env bash

permedcoe execute application app.py ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
                                     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
                                     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/config \
                                     --workflow_manager pycompss --flags "-d -g --python_interpreter=python3"

# Using shortcuts:
# permedcoe x app app.py ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
#                        ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
#                        ~/github/projects/PerMedCoE/Lysozyme_in_water/application/config \
#                        -w pycompss --flags "-d -g --python_interpreter=python3"

# Explicit call with PyCOMPSs runcompss command:
# runcompss -d -g --python_interpreter=python3 \
#     app.py \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/config
