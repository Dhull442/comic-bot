#!/bin/bash
st="19790101"
end=$(date +%Y%m%d)
tot=$(( ($(date --date="$end" +%s) - $(date --date="$st" +%s) )/(60*60*24) ))
day=$(( ( RANDOM % $tot )  + 1 ))
current=$(date -d "$st")
need=$(date -d "$current +$day day" +%Y%m%d)
# echo $need
link="http://images.ucomics.com/comics/ga/${need:0:4}/ga${need:2:6}.gif"
# echo $link
wget $link -O garfield.png -q
