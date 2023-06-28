
set -e
mkdir -p out
cd out
dataset_folder=../../dataset_small/
config_folder=../../config
output_folder=.
logfile=../out.log
protein=1u3m

set -x
echo "Generating topology"
generate_topology_BB --pdb $dataset_folder/${protein}.pdb --structure $output_folder/${protein}.gro --topology $output_folder/${protein}.top --topology_itp $output_folder/${protein}_top.itp &>> $logfile
echo "Defining box"
define_box_BB --structure $output_folder/${protein}.gro --structure_newbox $output_folder/${protein}_newbox.gro &>> $logfile
echo "Adding solvate"
add_solvate_BB --structure_newbox $output_folder/${protein}_newbox.gro --topology $output_folder/${protein}.top --protein_solv $output_folder/${protein}_solv.gro &>> $logfile
echo "Assembling"
assemble_tpr_BB --ions_conf $config_folder/ions.mdp --protein_solv $output_folder/${protein}_solv.gro --topology $output_folder/${protein}.top  --group $output_folder/${protein}_ions.tpr  &>> $logfile
echo "Replacing solvent"
replace_solvent_with_ions_BB --ions $output_folder/${protein}_ions.tpr --topology $output_folder/${protein}.top --group $config_folder/genion.group --protein_solv_ions $output_folder/${protein}_solv_ions.gro &>> $logfile
echo "Assembling"
assemble_tpr_BB --ions_conf $config_folder/minim.mdp --protein_solv $output_folder/${protein}_solv_ions.gro --topology $output_folder/${protein}.top --group $output_folder/${protein}_em.tpr     &>> $logfile
echo "Minimizing energy"
energy_minimization_BB --steps 100 --energy $output_folder/${protein}_em.tpr --structure $output_folder/${protein}_em.gro --file $output_folder/${protein}_em.edr --log $output_folder/${protein}_em.log --trajectory $output_folder/${protein}_em.trr &>> $logfile
echo "Analysing energy"
energy_analysis_BB --em_energy $output_folder/${protein}_em.edr --energy_selection $config_folder/energy.selection --energy_result $output_folder/${protein}_potential.xvg  &>> $logfile
echo "Equilibrating"
equilibrate_BB --conf $config_folder/nvt.mdp --structure_file $output_folder/${protein}_em.gro --structure2_file $output_folder/${protein}_em.gro --topology $output_folder/${protein}.top --result $output_folder/${protein}_nvt.tpr  &>> $logfile
echo "Minimizing energy"
energy_minimization_BB --steps 100 --energy $output_folder/${protein}_nvt.tpr --structure $output_folder/${protein}_eq.gro --file $output_folder/${protein}_eq.edr --log $output_folder/${protein}_eq.log --trajectory $output_folder/${protein}_eq.trr  &>> $logfile
echo "Analysing energy"
energy_analysis_BB --em_energy $output_folder/${protein}_eq.edr --energy_selection $config_folder/temperature.selection --energy_result $output_folder/${protein}_temperature.xvg  &>> $logfile
