#!/usr/bin/env bash

echo "Uninstalling..."

# python3 -m pip uninstall gromacs_BB

xargs rm -rf < installed_files.txt

rm installed_files.txt

echo "----- Uninstall finished -----"