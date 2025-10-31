# Testbed
To have fdp enabled kernel, fdp related kernel patch is needed.

## FDP kernel patch
https://github.com/SamsungDS/linux/commit/879822d2528090ce45bb54c4bf66344290fe037a

## filebench 
Once the FDP related kernel patch is installed,

run
```
sudo ./f2fs_mount.sh
```
then
```
sudo ./run_f2fs_fileserver.sh
```

for OLTP,
```
sudo ./run_f2fs_oltp.sh
```

