#!/bin/bash

sudo fio --name=trim --filename=/dev/nvme1n1 --rw=trim --bs=3G
sleep 60

sudo fio --name=trim --filename=/dev/nvme1n1 --rw=trim --bs=3G --size=140%
sleep 60
