#!/bin/bash

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
        echo "** Trapped CTRL-C"
        exit 0
}

ssh root@10.0.0.1
file=$1;
## shellcheck disable=SC2034
#while ( (i=7;i<=12;i++) ); do
#  sleep 3s;
#  rssi=`iw dev wlan0 station dump | grep "signal:" | tail -n 1 | awk '{print $2}'`;
#  echo $rssi >> $file;
#done
for ((i=1;i<=400;i++)); do
  # echo $(ssh root@10.0.0.1 iw dev wlan0 station dump | grep "signal:" | tail -n 1 | awk '{print $2}') >> $file
  echo action
  sleep 2s;
done