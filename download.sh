#!/bin/bash
while read i; do
	cd ./before_process
	wget $i;
	cd ..
done <urls.txt
