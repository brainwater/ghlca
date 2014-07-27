#!/bin/bash

# Imports csv files into database

# arg1: name of collection (e.g. max-watchers-repos or max-forks-repos)
# arg2: path to csv file

mongoimport --type csv --headerline --db ghlca --collection "${1}" "${2}"

