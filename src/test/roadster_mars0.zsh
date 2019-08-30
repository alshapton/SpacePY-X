echo "hello " $1 > fred
case $1 in
  marsDistance)
      cat data/roadster/roadster.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $5}'
      ;;
  speed)
      cat data/roadster/roadster.mars  | awk '/SOE/,/EOE/'  | awk 'NR==2 {print $7}'
      ;;
esac
