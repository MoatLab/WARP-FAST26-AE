#!/bin/bash
#mkdir -p ./tmp
#config_dir="/home/inho/git/CacheLib/cachelib/cachebench"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib/tmp"
config_dir="./configs"
output_dir="./results"
fdev="/dev/nvme2"
fdevname="nvme2"
#bin_dir="~/git/CacheLib/opt/cachelib/bin/"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/default/samsung"
#########################################
#               1. trim.sh              #
#########################################
sudo ./trim_${fdevname}.sh
sleep 1000
#########################################
#                2. run                 #
#########################################
# ------------ monitoring ------------ #
sudo ./5.get_waf_${fdevname}.sh &
wakeup_pid=$!
sudo ./6.get_bw_${fdevname}.sh &
wakeup_pid2=$!
echo "get_waf.sh PID:  $wakeup_pid"
echo "get_bw.sh PID :  $wakeup_pid2"
# ------------ cachebench ------------ #
sudo ./cachebench \
 -json_test_config ${config_dir}/fdp_enabled_config_soc20_super_SETONLY.json \
 -progress_stats_file=${output_dir}/kvcache202401_soc20_fdp.log 
# --------------- kill --------------- #
sleep 2000
echo "kill $wakeup_pid"
sudo kill $wakeup_pid
echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2
