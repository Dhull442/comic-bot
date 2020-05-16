wget -q http://explosm.net/comics/random -O index.html
file="$(cat index.html | tr '\"' '\n' | grep http://files.explosm.net/comics/ | head -n 1)"
rm index.html
wget $file -O ch.png -q
