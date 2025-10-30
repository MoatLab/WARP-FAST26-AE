
# Status
cdn2025     - Available.
kv202206    - Available. 
kv202210    - Available.
kv202410    - Available. 
twitter     - TBD 

## How to Download Traces

```
inho@hds03:.../scripts$ aws s3 ls --no-sign-request s3://cachelib-workload-sharing/pub/kvcache/
                           PRE 202206/
                           PRE 202210/
                           PRE 202401/
                           PRE Flat-12-06-2023/
                           PRE Flat_202312/
2023-02-09 21:27:48          0
aws s3 cp --no-sign-request --recursive s3://cachelib-workload-sharing/pub/kvcache/[trace e.g.,202401]/ [dirs_you_want]
```
