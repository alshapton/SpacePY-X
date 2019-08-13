if  [$1 = '2.7']
then
  pip install future --user
fi
python$1 -m pytest
