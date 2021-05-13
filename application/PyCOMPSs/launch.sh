#!/usr/bin/env bash

enqueue_compss \
    --job_name=Lysozyme_in_water \
    --num_nodes=2 \
    --exec_time=10 \
    --worker_working_dir=/gpfs/projects/bsc19/bsc19234/tmp/ \
    --scheduler=es.bsc.compss.scheduler.fifodatalocation.FIFODataLocationScheduler \
    --qos=debug \
    -t \
    --python_interpreter=python3 \
    app.py ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/dataset \
        ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/output \
        ~/PROJECTS/PerMedCoE/Lysozyme_in_water/application/config
