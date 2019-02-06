#!/bin/sh

AUDIOPATH="./audio/newtest.wav" 
SERVICE="omxplayer"
counter=0
while true; do
	if ps ax | grep -v grep | grep $SERVICE  > /dev/null
	then
	sleep 1;
else
	for entry in $AUDIOPATH
	do
		clear
		omxplayer -o local $entry > /dev/null
		counter=$((counter+1))
		echo "message was played $counter times"
	done
fi
done