#!/bin/sh

# Script to convert the raw cut 'n' paste from the Postman Docs for SpaceX API into insert-able documents for the matrix.json TinyDB.

# There are NO parameters.

# Start with the template
OUTPUT="matrix.py"
cp matrix.template.py $OUTPUT

# ALL the *.in files are the same format -
#     i)    Create/Edit a file called <function>.<subfunction>.in
#     ii)   Go to the correct Postman page for the SpaceX documents
#     iii)  Copy all tables associated with the function and insert into the file.
#     iv)   Save the file

#Iterate through all *.in files in the directory.

for FILENAME in parametersIN/*.in;
  do


  # Get the function/subfunction from the filename
	FUNCTION=`echo ${FILENAME} | cut -d"." -f1 | sed "s/parametersIN\///"`
	SUBFUNCTION=`echo ${FILENAME} | cut -d"." -f2`

  # Setup the beginning and end of the records
	INSERTSTART=`echo "db.insert({\"function\":\"$FUNCTION"\",\"subfunction\":\"$SUBFUNCTION"\",\"parameters\":["`
	INSERTEND="]})"

  # Parse each record and append to the $OUTPUT file.
	echo $(echo $INSERTSTART; cat $FILENAME |awk '$0="{\"parameter\":\""$0"\"},"' | sed "s/$(echo '\t')/\",\"example\":\"/"| sed "s/$(echo '\t')/\",\"type\":\"/" | sed "s/$(echo '\t')/\",\"comment\":\"/" | sed "s/\"integer\"/\"int\"/" | sed "s/\"boolean\"/\"bool\"/"| sed "s/\"string\"/\"str\"/" | sed "s/\"UTC ISO timestamp\"/\"timestamp\"/" ; echo $INSERTEND) | sed "s/, ]})/]})/" >> $OUTPUT
  done

# Now create the matrixDB.json database

python matrix.py


# Copy the database to the correct locations:

cp matrixDB.json ../spacexpython
cp matrixDB.json ../test
