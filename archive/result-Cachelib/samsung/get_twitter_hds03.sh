#!/bin/bash

echo "Processing twitter-cluster12 ...."
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme1_waf_1min.txt  twitter-cluster12/fdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme1_bw_1min.txt  twitter-cluster12/fdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme3_waf_1min.txt  twitter-cluster12/nofdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme3_waf_1min.txt  twitter-cluster12/nofdp/.


echo "Processing twitter-cluster37 ....."
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme5_waf_1min.txt  twitter-cluster37/fdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme5_bw_1min.txt  twitter-cluster37/fdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme6_waf_1min.txt  twitter-cluster37/nofdp/.
rsync hds03:/home/inho/git/CacheLib/inho-run-cachelib/fdp_vs_nofdp/samsung/nofdp/twitter/nvme6_waf_1min.txt  twitter-cluster37/nofdp/.
echo "Done"


