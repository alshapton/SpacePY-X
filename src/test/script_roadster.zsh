#!/bin/bash
# Script to extract values from JPL's Horizon's batch output
#
# Parameters
# ----------
#   extraction required : (string)
#
# Return
# ------
#   value(s) depending on the required input parameter
#

REQUIRED_VALUE=$1
BASE="roadster"

case $REQUIRED_VALUE in
  marsDistance)
      # Extract the roadster's distance from Mars
      cat $BASE.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $5}'
      ;;
  earthDistance)
      # Extract the roadster's distance from Earth
      cat $BASE.earth  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $5}'
      ;;
  speed)
      # Extract the roadster's orbital speed
      cat $BASE.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $7}'
      ;;
  epoch)
      # Extract the EPOCH from the orbit file
      cat $BASE.orbit | grep "EPOCH=" | awk '{print $2}'
      ;;
  sma)
      # Extract semi-major axis
      cat $BASE.orbit | grep "A =" | awk 'NR==2 {print $3}'
      ;;
  ec)
      # Extract eccentricity
      cat $BASE.orbit | grep " EC=" | awk 'NR==2 {print $2}'
      ;;
  qr)
      # Extract periapsis
      cat $BASE.orbit | grep " QR=" | awk 'NR==2 {print $4}'
      ;;
  ad)
      # Extract apoapsis
      cat $BASE.orbit | grep " AD=" | awk 'NR==2 {print $5}'
      ;;
  om)
      # Extract Longitude of Ascending Node
      cat $BASE.orbit | grep " OM=" | awk 'NR==2 {print $2}'
      ;;
  w)
      # Extract Eperiapsis Argument
      cat $BASE.orbit | grep " OM=" | awk 'NR==2 {print $5}'
      #
      # Even though the requirement is to get the 'W' field, the best tracing mechanism is to find the 'OM' lines
      #
      ;;
  inc)
      # Extract Longitude of Ascending Node
      cat $BASE.orbit | grep " IN=" | awk 'NR==2 {print $6}'
      ;;
  period)
      # Extract period
      cat $BASE.orbit | grep " PR=" | awk 'NR==2 {print $7}'
esac
