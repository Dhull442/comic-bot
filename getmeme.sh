wget http://explosm.net/rcg -O rcg -q
file="$(cat rcg | tr '\"' '\n' | grep rcg-cdn | head -1)"
rm rcg
wget "$file" -O img.png -q
