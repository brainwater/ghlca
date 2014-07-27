#!/bin/bash

# Formats the csv files by removing the a_ prefix from the header

# arg1: input file
# arg2: output file

head -n 1 "${1}" | sed -e "s/^a_//" -e "s/,a_/,/g" > "${2}"
tail -n +2 "${1}" >> "${2}"

