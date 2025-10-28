# Device Path

Make sure 
1. .json config file  ['nvmeXn1']
2. run_nofdp4_kvcache_FULL.sh file's .json config file matches
3. 5.get_waf.sh WAF file device path 'nvmeXn1'
4. trim.sh device path 'nvmeXn1'

# To run
prepare  'cachebench' binary to run.

For example
```
inho@hds03:~/.../kvcache202401$ pwd
/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/kvcache202401
inho@hds03:~/.../kvcache202401$ ls -lha
drwxrwxr-x  2 inho inho 4.0K Aug 30 06:51 configs
drwxrwxr-x  4 inho inho 4.0K Aug 30 07:10 results
lrwxrwxrwx  1 inho inho   51 Aug 28 05:02 cachebench -> /home/inho/git/CacheLib/opt/cachelib/bin/cachebench
```

Then
```
sudo nohup ./run_fdp4_kvcache_FULL.sh & 
```
or plainly,
```
sudo ./run_fdp4_kvcache_FULL.sh
```
