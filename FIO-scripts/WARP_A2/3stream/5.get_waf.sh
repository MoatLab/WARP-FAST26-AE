#!/bin/bash
target_file="samsung_waf_1sec.txt"
dev="/dev/ng0n1"
#output_dir="/home/inho/git/CacheLib/inho-run-cachelib"
#mv_dir="/home/inho/git/CacheLib/inho-run-cachelib/fadu-full-noFDP"

while true
do
    date>>./${target_file}
    sudo nvme fdp stats -e 1 ${dev} >> ./${target_file}
    sudo nvme fdp usage -e 1 ${dev} >> ./${target_file}
    sleep 1
done
