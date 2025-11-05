#!/bin/bash
if [ "$#" -ne 1 ] ; then  
    echo "provide \"/dev/nvmeX\" for running script."
    echo "  e.g., $0 /dev/nvme0"
fi

echo "Start to setup FDP device $1 ..."
#1. Validate the FDP capability. 19th bit on.
echo "1. Validate the FDP capability. 19th bit on"
sudo nvme id-ctrl $1 | grep -i ctratt

#2. Delete NSs in the endurance group
echo "2. Delete NSs in the endurance group"
sudo nvme delete-ns $1 -n 1

#3. Get log page command to print configs
echo "3. Get log page command to print configs"
nvme fdp configs $1 -e 1 -H

#4. Enable FDP with config 0 
echo "4. Enable FDP with config 0"
nvme set-feature $1 -f 0x1D -c 1 -s 

#5. This should print out whether FDP is enabled
echo "5. This should print out whether FDP is enabled"
nvme get-feature $1 -f 0x1D -H

#6.Create an ns
echo "6. Create ns with fdp" 
NSZE=$(sudo nvme id-ctrl $1 | grep -i tnvmcap | sed "s/,//g" | awk '{print $3/4096}');
sudo nvme create-ns $1 -b 4096 --nsze=$NSZE --ncap=$NSZE -p 0,1,2,3,4,5,6 -n 7
echo "   Attaching ns.... (Note ; for FADU, controllers=0x1)"
sudo nvme attach-ns $1 --namespace-id=1 --controllers=0x1

echo "7. done. "
sudo nvme id-ctrl $1 | grep oacs
echo "Hello, fdp world!"
