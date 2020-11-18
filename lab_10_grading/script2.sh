#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
var1=".sh"
var2="Makefile"
for entry in "$DIR"/*
do
	if [[ "$entry" != *"$var1" && "$entry" != *"$var2" ]]; then
  		temp="$entry"
	fi
done
rm -rf $temp
