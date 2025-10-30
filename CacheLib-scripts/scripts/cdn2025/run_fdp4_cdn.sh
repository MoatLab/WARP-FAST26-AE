#!/bin/bash
#mkdir -p ./tmp
#config_dir="/home/inho/git/CacheLib/cachelib/cachebench"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib/tmp"
config_dir="./configs"
output_dir="./results"
fdev="/dev/nvme3"
fdevname="nvme3"
#bin_dir="~/git/CacheLib/opt/cachelib/bin/"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/default/samsung"
#########################################
#               1. trim.sh              #
#########################################
#sudo ./trim_${fdevname}.sh
#sleep 600
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
 -json_test_config ${config_dir}/fdp4_bigcache_trace_sea1c01_20250414_20250421.json \
 -progress_stats_file=${output_dir}/cdn_soc4_fdp.log 
# --------------- kill --------------- #
sleep 2000
echo "kill $wakeup_pid"
sudo kill $wakeup_pid
echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2
