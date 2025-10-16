#!/bin/bash
rsync vm2:/home/inhoinno/filebench-1.5-alpha3/inho_scripts/scripts_fdp/samsung_bw_1sec.txt cylon/fdp/.
rsync vm2:/home/inhoinno/filebench-1.5-alpha3/inho_scripts/scripts_fdp/samsung_waf_1sec.txt cylon/fdp/.
#rsync vm2:/home/inhoinno/filebench-1.5-alpha3/inho_scripts/scripts_fdp/femu_waf_1sec.txt cylon/fdp/.

rsync vm:/home/inhoinno/filebench-1.5-alpha3/scripts_fdp/samsung_waf_1sec.txt  cylon/nofdp/.
rsync vm:/home/inhoinno/filebench-1.5-alpha3/scripts_fdp/samsung_bw_1sec.txt  cylon/nofdp/.

#mv cylon/fdp/femu_waf_1sec.txt cylon/fdp/samsung_waf_1sec.txt
