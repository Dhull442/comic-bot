wget http://www.bunicomic.com/?random -O buni -q
file="$(cat buni | tr '\"' '\n'| grep http://www.bunicomic.com/wp-content/uploads/ | head -n 1)"
rm buni
wget $file -O buni.png -q
