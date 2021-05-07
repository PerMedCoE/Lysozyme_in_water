#!/usr/bin/env bash

permedcoe execute application app.py ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
                                     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
                                     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/application/config

# Using shortcuts:
# permedcoe x app app.py

# Explicit call:
# python3 \
#     app.py \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/dataset \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/output \
#     ~/github/projects/PerMedCoE/Lysozyme_in_water/application/config
