#!/bin/bash
size_tag="K"
#cmd="python3 w_fiogen.py"
#echo ${cmd}
#${cmd}

workload_file=( "1stream.fio" )

for i in ${!workload_file[@]}
do

#sudo ./trim.sh
#sleep 1200
sudo ./5.get_waf.sh &
wakeup_pid=$!
sudo ./6.get_bw.sh &
wakeup_pid2=$!
echo "get_waf.sh PID:  $wakeup_pid"
echo "get_bw.sh PID :  $wakeup_pid2"

bs=16
qd=4

cmd="sudo fio ${workload_file[i]}"
echo ${cmd}
${cmd} >> 1threadQD${qd}_${bs}${size_tag}write_output
sleep 0.1

sleep 1
echo "kill $wakeup_pid"
sudo kill $wakeup_pid

echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2


#mv samsung* ./"${workload_dir[i]}"/.
#mv 1thread* ./"${workload_dir[i]}"/.
#fio_generate_plots ${bs}${size_tage} 1threadQD${qd}_${bs}${size_tag}randreadfiles_lat.1.log
done

