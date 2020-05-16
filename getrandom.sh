#!/bin/bash
# # blm 19801208
# # ga 19790101
# # ca 19960501
# # dt 20120201
# # fm 20120101
# # fb 20120102
# # bl 20120102
# lu
# nq
# of
# pb
# rr
# bo
# wiz
st="20120201"
end=$(date +%Y%m%d)
tot=$(( ($(date --date="$end" +%s) - $(date --date="$st" +%s) )/(60*60*24) ))
day=$(( ( RANDOM % $tot )))
current=$(date -d "$st")
need=$(date -d "$current +$day day" +%Y%m%d)
id=$(( ( RANDOM % $17 )  + 1 ))
id="$(sed -n ${id}p ids)"
# echo $need
link="http://images.ucomics.com/comics/$id/${need:0:4}/${id}${need:2:6}.gif"
echo $link
# echo $link
wget $link -O random.png -q
