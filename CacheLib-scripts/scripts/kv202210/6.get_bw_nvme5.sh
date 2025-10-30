#!/bin/bash
target_file="samsung_bw_1min.txt"
output_dir="./"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/samsung-full-noFDP"

while true
do
    date>>${output_dir}/${target_file}
    iostat nvme4n1
    iostat nvme4n1 >> ${output_dir}/${target_file}
    sleep 60
done
