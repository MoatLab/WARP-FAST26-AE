#!/bin/bash
#mkdir -p ./tmp
#config_dir="/home/inho/git/CacheLib/cachelib/cachebench"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib/tmp"
config_dir="./scripts/"
output_dir="./results/"
#bin_dir="~/git/CacheLib/opt/cachelib/bin/"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/default/samsung"
#########################################
#               1. trim.sh              #
#########################################
sudo ./trim_nvme5.sh
sleep 1000
#########################################
#                2. run                 #
#########################################
# ------------ monitoring ------------ #

sudo ./5.get_waf_nvme5.sh &
wakeup_pid=$!
sudo ./6.get_bw_nvme5.sh &
wakeup_pid2=$!
echo "get_waf.sh PID:  $wakeup_pid"
echo "get_bw.sh PID :  $wakeup_pid2"
# ------------ cachebench ------------ #

sudo ./cachebench \
 -json_test_config ${config_dir}/nofdp_disabled_config_soc20_excel_FULL.json \
 -progress_stats_file=${output_dir}/kvcache202206_nofdp_soc20.log 

# --------------- kill --------------- #
sleep 2000
echo "kill $wakeup_pid"
sudo kill $wakeup_pid
echo "kill $wakeup_pid2"
sudo kill $wakeup_pid2
