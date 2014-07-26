#!/bin/bash

# Pipe in the repository names to download, it will download them in the current directory.

while read repo
do
    pth="$(echo "${repo}" | sed -e "s_https://github.com/__").git"
    #mkdir -p "${pth}"
    git clone --bare "${repo}" "${pth}"
done
