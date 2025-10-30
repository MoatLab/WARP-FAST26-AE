#!/bin/bash
target_file="nvme0_bw_1sec.txt"
dev="/dev/nvme0n1"

#while true
#do
iostat -d ${dev} -m 1 >> ./${target_file}
#done
