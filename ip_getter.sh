#!/bin/bash
set -x

ip=$(curl ifconfig.me)

echo $ip > "new_ip.txt"

#sudo chmod -R 0655 teletest.sh
