#!/bin/bash

H=$(cat nvme3_waf_1min.txt | head -4 | sed 's/,//g' | awk '{print $7}' | head -n1)
M=$(cat nvme3_waf_1min.txt | tail -4 | sed 's/,//g' | awk '{print $7}' | tail -n3)

# math (integer)
wrt_tib=$(( (M - H) / (2**40) ))
rhmw_x=$(( wrt_tib / 8 ))
color=$red
if (( rhmw_x > 5 )); then
  color=$green
fi
printf '%s$(1) %s TiB, ~rhmw=x%s  %s%s\n' \
  "$color" "$wrt_tib" "$rhmw_x" "$(( first - second ))" "$reset"


