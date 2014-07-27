#!/bin/bash

# Pipe in the repository names to download, it will download them in the current directory.
# arg1: path to download the repos to (e.g. ~/data/ghlca/repos)

if cd "${1}"
then
    while read repo
    do
	pth="$(echo "${repo}" | sed -e "s_https://github.com/__").git"
	repo="$(echo "${repo}" | sed -e "s/https/git/")"
	if [ -e "${pth}/config" ]
	then
	    echo "Skipping existing repo ${repo}"
	else
	    if [ -e "${pth}" ]
	    then
		rm -rf "${pth}"
	    fi
	    echo "Cloning repository ${repo} into ${pth}"
	    git clone -q --bare "${repo}" "${pth}"
	fi
    done
fi
