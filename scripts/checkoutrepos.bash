#!/bin/bash
cd ~/data/ghlca/repos/wtch

for own in *
do
    mkdir "/home/blake/data/ghlca/files/wtch/${own}"
    cd "/home/blake/data/ghlca/repos/wtch/${own}"
    for nam in *
    do
	echo "${own}/${nam}"
	cd "/home/blake/data/ghlca/files/wtch/${own}"
	git clone -q "/home/blake/data/ghlca/repos/wtch/${own}/${nam}"
	rm -rf "/home/blake/data/ghlca/repos/wtch/${own}/${nam}/.git"
    done
done
