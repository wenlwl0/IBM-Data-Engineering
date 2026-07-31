#!/bin/bash

echo 'Do you drive?'
echo -n "Enter \"y\" for yes, \"n\" for no."
read response
if [ "$response" = "y" ]
then
    echo "Drive safely"
	echo "Don't speed"
elif [ "$response" = "n" ]
then
   echo "Sign up for driving lessons!"
else
   echo "Your response must be either 'y' or 'n'."
   echo "Please re-run the script to try again."
fi
