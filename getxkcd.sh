wget https://c.xkcd.com/random/comic/ -O xkcd -q
file="$(cat xkcd | tr '\"' '\n' | grep //imgs.xkcd.com/comics/ | sed -n 2p)"
rm xkcd
wget "https:$file" -O xkcd.png  -q
