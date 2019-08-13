VERSION=`echo $1 | cut -c1-4`
if  [$VERSION = '2.7']
then
  pip install future --user
fi
python$VERSION -m pytest
