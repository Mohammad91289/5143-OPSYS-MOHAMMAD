#!/bin/bash
file=/usr/share/dict/words
# To calculate the number of words in file
words_total=$(wc -l $file | awk '{print $1}')
#calculating random number
random_line_num=$(($(cat /dev/random | od -N3 -An -D) % $words_total))
echo "The Random line number generated is:"$random_line_num
#Print the random word as per the random number calcutlated above
awk 'NR == $random_line_num {print $0;}' "$file"
#awk -n '$random_line_num ' $file
#echo $NR
#final_word='sed -n $file'
#echo $final_word
