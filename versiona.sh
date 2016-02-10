#!/bin/bash


#reading the First argument as filename
filename=$1
echo "the first argument passed is:"$filename

#creating a newfile
date1=$(date +"%Y-%M-%D")
undscr="_"
newfile="$date1$undscr$filename"

#Copying Filename
cp $filename $newfile
echo "The newfile created is:"$newfile

