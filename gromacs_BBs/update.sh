SOURCE="$(pwd)/equilibrate/"

grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/equilibrate/g'
grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/equilibrate/g'
grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Equilibrate/g'
grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/equilibrate/g'
grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/EQUILIBRATE/g'
mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/equilibrate_BB


# SOURCE="$(pwd)/define_box/"
#
# grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/define_box/g'
# grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/define box/g'
# grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Define Box/g'
# grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/define-box/g'
# grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/DEFINE_BOX/g'
# mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/define_box_BB
#
# SOURCE="$(pwd)/energy_analysis/"
#
# grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/energy_analysis/g'
# grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/energy analysis/g'
# grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Energy Analysis/g'
# grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/energy-analysis/g'
# grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/ENERGY_ANALYSIS/g'
# mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/energy_analysis_BB
#
# SOURCE="$(pwd)/energy_minimization/"
#
# grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/energy_minimization/g'
# grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/energy minimization/g'
# grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Energy Minimization/g'
# grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/energy-minimization/g'
# grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/ENERGY_MINIMIZATION/g'
# mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/energy_minimization_BB
#
# SOURCE="$(pwd)/generate_topology/"
#
# grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/generate_topology/g'
# grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/generate topology/g'
# grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Generate Topology/g'
# grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/generate-topology/g'
# grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/GENERATE_TOPOLOGY/g'
# mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/generate_topology_BB
#
# SOURCE="$(pwd)/replace_solvent_with_ions/"
#
# grep -rl "add_solvate" ${SOURCE} | xargs sed -i 's/add_solvate/replace_solvent_with_ions/g'
# grep -rl "add solvate" ${SOURCE} | xargs sed -i 's/add solvate/replace solvent with ions/g'
# grep -rl "Add Solvate" ${SOURCE} | xargs sed -i 's/Add Solvate/Replace Solvent with Ions/g'
# grep -rl "add-solvate" ${SOURCE} | xargs sed -i 's/add-solvate/replace-solvent-with-ions/g'
# grep -rl "ADD_SOLVATE" ${SOURCE} | xargs sed -i 's/ADD_SOLVATE/REPLACE-SOLVENT-WITH-IONS/g'
# mv ${SOURCE}/src/add_solvate_BB ${SOURCE}/src/replace_solvent_with_ions_BB
