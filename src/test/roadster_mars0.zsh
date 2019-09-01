#!/bin/bash
# Script to extract values from JPL's Horizon's batch output
#
# Parameters

echo $1 > fred
REQUIRED_VALUE=$1
case $REQUIRED_VALUE in
  marsDistance)
      # Extract the roadster's distance from Mars
      cat data/roadster/roadster.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $5}'
      ;;
  speed)
      # Extract the roadster's orbital speed
      cat data/roadster/roadster.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $7}'
      ;;
  epoch)
    # Extract the EPOCH from the orbit file
    cat data/roadster/roadster.orbit | grep "EPOCH=" | awk '{print $2}'
esac
