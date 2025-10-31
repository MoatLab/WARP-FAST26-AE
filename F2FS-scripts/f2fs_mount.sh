#!/bin/bash


mkfs.f2fs -f /dev/nvme0n1 
mount /dev/nvme0n1 /mnt/f2fs

