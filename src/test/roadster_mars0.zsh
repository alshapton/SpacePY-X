#!/bin/bash
# Script to extract values from JPL's Horizon's batch output
#
# Parameters


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
esac
