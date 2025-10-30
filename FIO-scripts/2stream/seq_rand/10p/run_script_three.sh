#!/bin/bash
size_tag="K"
#cmd="python3 w_fiogen.py"
#echo ${cmd}
#${cmd}

workload_dir=("nofdp" "fdp" "fdp_share")
#workload_dir=("fdp_share_v2")
workload_file=("py_randwritefiles_bs4K_QD4_t0" "py_randwritefiles_bs4K_QD4_fdp" "py_randwritefiles_bs4K_QD4_fdp_share" )
#workload_file=( "py_randwritefiles_bs4K_QD4_fdp_share" )

for i in ${!workload_file[@]}
do

sudo ./trim.sh
sleep 1200
sudo ./5.get_waf.sh &
wakeup_pid=$!
sudo ./6.get_bw.sh &
wakeup_pid2=$!
echo "get_waf.sh PID:  $wakeup_pid"
echo "get_bw.sh PID :  $wakeup_pid2"

bs=16
#qd=$((2**i))
qd=4
#size=$((10*(k-1)))
#size=$((100 + (100*k)))
#cmd="sudo fio py_randwritefiles_bs${bs}K_QD${qd}_s${size}"
#cmd="sudo fio py_randwritefiles_bs${bs}K_QD${qd}"
#for j in {1 2}
#do

cmd="sudo fio ${workload_file[i]}"
echo ${cmd}
${cmd} >> 1threadQD${qd}_${bs}${size_tag}write_output
sleep 0.1

sleep 1200
echo "kill $wakeup_pid"
sudo kill $wakeup_pid

echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2


mv samsung* ./"${workload_dir[i]}"/.
mv 1thread* ./"${workload_dir[i]}"/.

#fio_generate_plots ${bs}${size_tage} 1threadQD${qd}_${bs}${size_tag}randreadfiles_lat.1.log
done

