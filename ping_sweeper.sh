#!/bin/bash
# Script that performs a ping sweep of a target IP range of form 192.168.1.0/24

if [ -z "$1" ]
then
  echo "Usage: ./pingsweep.sh 192.168.1.0/24"
else
  addr_string=$(echo $1 | awk -F "." '{print $1"."$2"."$3}')
  
  if [ -n "$addr_string" ]
  then
    for i in {1..254}
    do
      ping_response=$(ping -n -c 1 -W 0.3 $addr_string.$i | grep "64 bytes")
  
      if [ -n "$ping_response" ]
      then
        echo "$addr_string.$i is up"
      fi  
    done
   fi
fi
