#!/bin/sh 
FUNCTION=$1
SUBFUNCTION=$2

INSERTSTART=`echo "db.insert({\"function\":\"$FUNCTION"\",\"subfunction\":\"$SUBFUNCTION"\",\"parameters\":["`
INSERTEND="]})"


echo $(echo $INSERTSTART; cat cores.txt |awk '$0="{\"parameter\":\""$0"\"},"' | sed "s/$(echo '\t')/\",\"example\":\"/"| sed "s/$(echo '\t')/\",\"type\":\"/" | sed "s/$(echo '\t')/\",\"comment\":\"/" | sed "s/\"integer\"/\"int\"/" | sed "s/\"boolean\"/\"bool\"/" | sed "s/\"UTC ISO timestamp\"/\"timestamp\"/" ; echo $INSERTEND) | sed "s/, ]})/]})/"


