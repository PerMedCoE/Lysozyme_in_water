#!/usr/bin/env bash

permedcoe execute application app.py /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/dataset \
                                     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/output \
                                     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/config

# Using shortcuts:
# permedcoe x app app.py

# Explicit call:
# python3 \
#     app.py \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/dataset \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/output \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/config