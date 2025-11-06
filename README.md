
# Experiment scripts for WARP
These are the scripts that I used for both FDP SSD and WARP(proj old name Cylon-FDP) testing.

Experiments are three-fold. FIO. CacheLib. and F2FS.

## FDP SSD setup (nvme cli)
```
sudo ./fdp_setup_nvme-cli.sh /dev/nvmeX
```

# Dependency 
## libnvme
I'm using `nvme fdp ` command to get the write amplification results
to use, libnvme should be v1.5

```
wget https://github.com/linux-nvme/libnvme/archive/refs/tags/v1.5.tar.gz
```
tar -xvf v1.5.tar.gz, then

```
meson setup .build
```



## liburing 
version 2.3 >= works fine

Also works fine with
v2.3
v2.6
v2.7
v2.9
v2.10


## FIO
version 3.36


## Kernel
Using 6.2.14

Also tested with
v6.5.6
v6.10.x (especially F2FS, 6.10.x)


