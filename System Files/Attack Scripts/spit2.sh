#!/bin/bash

command="python3 ./sipinvite.py -i 192.168.1.10 -tu 7000"
interval=10

while true; do
    $command

    if [ $? -ne 0 ]; then
        echo "Command failed with error: $?"
    fi
    sleep $interval
done