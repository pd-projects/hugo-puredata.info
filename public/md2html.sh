#!/bin/sh

dir0=$pwd

for f in $(find ./ -name '*.md'); do 

./pandoc -f markdown -t html5 "$f" --template "${dir0}template.txt" -o "${f%.*}".html

 
done




