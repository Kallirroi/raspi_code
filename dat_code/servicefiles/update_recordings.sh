#!/bin/bash

function start {
  echo  "Syncing recordings between nodes..."
  cd /home/pi/raspi_code/dat_code/recordings/
  cp *.wav /home/pi/raspi_code/recordings/
}
