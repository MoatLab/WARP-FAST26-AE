#!/bin/bash

#./trim.sh 
#sleep 100

#./f2fs_mount.sh
SCRIPT_DIR="filebench-workloads/"
echo 0 > /proc/sys/kernel/randomize_va_space

sudo ./5.get_waf.sh &
wakeup_pid=$!
sudo ./6.get_bw.sh &
wakeup_pid2=$!
echo "get_waf.sh PID:  $wakeup_pid"
echo "get_bw.sh PID :  $wakeup_pid2"

filebench -f ./$SCRIPT_DIR/fileserver-custom.f

sleep 100
echo "kill $wakeup_pid"
sudo kill $wakeup_pid

echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2

#mv samsung_* trial2/.
