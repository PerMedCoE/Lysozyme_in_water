#!/usr/bin/env bash

permedcoe execute application app.py /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/dataset \
                                     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/output \
                                     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/config \
                                     --workflow_manager pycompss --flags "-d -g --python_interpreter=python3"

# Using shortcuts:
# permedcoe x app app.py -w pycompss --flags "-d -g --python_interpreter=python3"

# Explicit call with PyCOMPSs runcompss command:
# runcompss -d -g --python_interpreter=python3 \
#     app.py \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/dataset \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/output \
#     /home/javier/gitlab/projects/permedcoe/lysozyme_in_water/config
