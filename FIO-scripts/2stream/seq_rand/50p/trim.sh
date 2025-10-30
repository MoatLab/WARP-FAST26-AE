#!/bin/bash
sudo fio --name=trim --filename=/dev/nvme0n1 --rw=trim --bs=3G
