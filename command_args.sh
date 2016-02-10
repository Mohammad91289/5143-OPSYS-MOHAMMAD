#!/bin/bash
# Script to read Command Line Arguments

echo "My First Bash Script"

echo "Reading Command Line Arguments"
# Lists all the arguments
echo "$@"
# Prints the Name of BashScript
echo "$0"
# Prints First argument
echo "$1"

echo "The number of arguments printed are:"
echo "$#"

echo "The End of arguments"
