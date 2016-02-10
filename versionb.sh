#!/bin/bash
##########################

filename=$1
fname="${filename##*/}"
ext="${filename##*.}"
date1=$(date +%y-%m-%d)
new_file="${fname%.*}_$date1.$ext"
cp $fname $new_file
echo "The New created file is:"$new_file

