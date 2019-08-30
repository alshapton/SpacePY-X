cat data/roadster/roadster.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $7}'
