#!/bin/sh

usage(){
	cat << EOF
Usage: $(basename $0) [-n NUM KEYWORD0 KEYWORD1 ...]

NUM number of keywords to generate graph from
KEYWORD do a wikipedia search on each keywoard

(Enter "keyword keyword" for two word keyword)

Script to run final data structures project that takes in number of keywords, followed by keywords.
It runs crawl.py and pipes output into philo.cpp, which takes in list of sites traversed and builds 
a graph from titles. It then uses the graphviz library to create a .dot file, and then create a 
visual .png file of an overall graph.

EOF
	exit $1
}

NUM=0
BENCHMARK=0
ARGS=""
NFLAG=0

# parse command line
while [ "$#" -gt 0 ]; do
	case $1 in
		-n) 
			NFLAG=$1
			shift
			NUM=$1
			;;
		-h)
			usage 0
			;;
		-b) # benchmark
			BENCHMARK=1
			shift
			;;
	esac
	ARGS+=" " # string of arguments to pipe into crawl.py
	ARGS+=$1
	shift
done

# echo $ARGS

echo Crawling Wikipedia...
echo " "

CRAWL=`./crawl.py $NFLAG $ARGS`

touch "graph.dot"

echo All traversed pages...
echo " "

echo $CRAWL

echo " "
echo Constructing a graph and .dot file...
echo " "

echo $CRAWL | `./philo`

echo Creating a .png file...
echo " "

`dot -T png -O graph.dot`	# create png from dot file


