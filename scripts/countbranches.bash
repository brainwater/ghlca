#!/bin/bash

repo="$(echo "${1}" | sed -e "s_https://github.com/*__").git"

cd "${repo}"
git branch -a | wc -l
