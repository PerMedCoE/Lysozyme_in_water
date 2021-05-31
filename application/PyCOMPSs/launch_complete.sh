#!/usr/bin/env bash

enqueue_compss \
    --job_name=Lysozyme_in_water \
    --num_nodes=3 \
    --exec_time=20 \
    -t \
    --python_interpreter=python3 \
    app_complete.py ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/dataset \
                    ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/output \
                    ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/config
