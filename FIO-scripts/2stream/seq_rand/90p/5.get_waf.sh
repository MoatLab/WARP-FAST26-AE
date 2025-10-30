#!/bin/bash
target_file="nvme0_waf_1sec.txt"
dev="/dev/ng0n1"

while true
do
    date>>./${target_file}
    sudo nvme fdp stats -e 1 ${dev} >> ./${target_file}
    sleep 1
done
