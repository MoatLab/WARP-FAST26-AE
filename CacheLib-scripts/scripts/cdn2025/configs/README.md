## Device path

Use this to see current device path
```
grep -rn 'nvme' 
```

To change, use command below
```
grep -rl 'nvmeX' | xargs sed -i 's/nvmeXn1/nvmeYn1/g'
```


## config file
For FDP, use

fdp4_bigcache_trace_sea1c01_20250414_20250421.json      # FDP enabled, soc 4%
fdp_bigcache_trace_sea1c01_20250414_20250421.json       # FDP enabled, soc 0% (CacheLib default)

For noFDP, use
nofdp4_bigcache_trace_sea1c01_20250414_20250421.json    # FDP disabled, soc 4% 
nofdp_bigcache_trace_sea1c01_20250414_20250421.json     # FDP disabled, soc 0% (CacheLib default)

## trace(.csv) file

Note : this scripts captures the .csv path specified in .json file

To use exactly the same .json config file, symbolic link should be located in this directory(cdn2025/configs/.)

```
lrwxrwxrwx 1 inho inho   58 Oct 30 19:10 sea1c01_20250414_20250421_1.0000.csv -> /data/inho/traces/cdn/sea1c01_20250414_20250421_1.0000.csv
```

This is what I see
```
inho@hds03:.../configs$ ll
total 28
drwxrwxr-x 2 inho inho 4096 Oct 30 19:10 ./
drwxrwxr-x 3 inho inho 4096 Oct 30 19:10 ../
-rw-rw-r-- 1 inho inho 3582 Oct 30 19:10 bigcache_trace_sea1c01_20250414_20250421.json
-rw-rw-r-- 1 inho inho 3807 Oct 30 19:10 fdp4_bigcache_trace_sea1c01_20250414_20250421.json
-rw-rw-r-- 1 inho inho 3768 Oct 30 19:10 fdp_bigcache_trace_sea1c01_20250414_20250421.json
-rw-rw-r-- 1 inho inho 3690 Oct 30 19:10 nofdp4_bigcache_trace_sea1c01_20250414_20250421.json
-rw-rw-r-- 1 inho inho 3671 Oct 30 19:10 nofdp_bigcache_trace_sea1c01_20250414_20250421.json
lrwxrwxrwx 1 inho inho   58 Oct 30 19:10 sea1c01_20250414_20250421_1.0000.csv -> /data/inho/traces/cdn/sea1c01_20250414_20250421_1.0000.csv

``` 
