cat roadster.output  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $5}'
