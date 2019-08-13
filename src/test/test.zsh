VERSION=`echo $1 | cut -c1-3`
MAJOR_VERSION=`echo $VERSION | cut -c1-1`
if  [ $VERSION = '2.7' ]
then
  pip install future --user
  MAJOR_VERSION=''
fi
echo "Python       Version: $VERSION \n"
echo "Python Major Version: $MAJOR_VERSION \n"
python$MAJOR_VERSION -m pytest
