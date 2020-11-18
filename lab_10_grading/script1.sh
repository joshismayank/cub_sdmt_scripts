#!/bin/bash
git clone "$1"
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
var1=".sh"
var2="Makefile"
for entry in "$DIR"/*
do
	if [[ "$entry" != *"$var1" && "$entry" != *"$var2" ]]; then
  		temp="$entry"
	fi
done
cd $(echo $temp | tr -d '\r')
cd lab_10 || cd Lab_10 || cd lab10 ||cd Lab10
PWDD="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
varnew=".html"
for entry in "$PWDD"/*
do
	if [[ "$entry" == *"$varnew" ]]; then
  		tempnew="$entry"
	fi
done
echo $tempnew
google-chrome $tempnew &
