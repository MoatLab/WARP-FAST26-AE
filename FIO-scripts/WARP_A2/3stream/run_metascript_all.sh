#!/bin/bash
size_tag="K"
#cmd="python3 w_fiogen.py"

current_directory=$(pwd)
working_dir="${current_directory}/"
superworkload_dir=( "zoned" "zipf_2.2" "zipf_1.2" "uniform" )
#superworkload_dir=("zipf_1.2" "zoned" "zipf_2.2" "zoned_QD16" "sq0_90r_zipf_1.2" "sq0_zipf_1.2" )

#workload_dir=("fdp" "fdp_share" "nofdp")
workload_dir=("fdp")
#workload_file=("py_randwritefiles_bs4K_QD4_fdp" "py_randwritefiles_bs4K_QD4_fdp_share" "py_randwritefiles_bs4K_QD4_t0")
workload_file=("py_randwritefiles_bs4K_QD4_fdp" )


for s in ${!superworkload_dir[@]}
do

echo "$working_dir/${superworkload_dir[s]}"

pushd .
cd "$working_dir/${superworkload_dir[s]}"

for i in ${!workload_file[@]}
do

sudo ./trim.sh > /dev/null

sleep 10
sudo ./5.get_waf.sh &
wakeup_pid=$!
#sudo ./6.get_bw.sh &
#wakeup_pid2=$!
echo "  get_waf.sh PID:  $wakeup_pid"
#echo "  get_bw.sh PID :  $wakeup_pid2"

bs=4
#qd=$((2**i))
qd=4
#size=$((10*(k-1)))
#size=$((100 + (100*k)))
#cmd="sudo fio py_randwritefiles_bs${bs}K_QD${qd}_s${size}"
#cmd="sudo fio py_randwritefiles_bs${bs}K_QD${qd}"
#for j in {1 2}
#do

cmd="sudo fio ${workload_file[i]}"

echo "  ${cmd}"
${cmd} >> 1threadQD${qd}_${bs}${size_tag}write_output
sleep 0.1

sleep 10
echo "kill $wakeup_pid"
sudo kill $wakeup_pid

echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2

mv samsung* ./"${workload_dir[i]}"/.
mv 1thread* ./"${workload_dir[i]}"/.

#fio_generate_plots ${bs}${size_tage} 1threadQD${qd}_${bs}${size_tag}randreadfiles_lat.1.log
done

popd

done
