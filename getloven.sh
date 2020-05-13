wget https://www.mrlovenstein.com/shuffle -O loven -q
file="$(cat loven  | tr '\"' '\n' | grep /images/comics/ | head -n 1)"
rm loven
wget "https://www.mrlovenstein.com$file" -O loven.png -q
