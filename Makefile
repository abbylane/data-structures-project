CC= g++
SHELL = bash
CFLAGS= -g -Wall -std=c++11
MEASURE= ./measure

all: 		philo measure

measure: measure.c
	gcc -Wall -std=gnu99 -o $@ $^

philo: philo.cpp
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -rf philo
	rm -rf measure

test: 	 test-output

test-output: 
	@echo Testing 1 keyword...
	@echo ./run.sh -n 1 apple
	@diff --suppress-common-lines -y <(./run.sh -n 1 apple) output1
	@echo " "
	@echo Testing 3 keywords...
	@echo ./run.sh -n 3 apple uggs pencil
	@diff --suppress-common-lines -y <(./run.sh -n 3 apple uggs pencil) output3
	@echo " "
	@echo Testing 5 keywords...
	@echo ./run.sh -n 1 apple uggs pencil water miley
	@diff --supress-common-lines -y <(./run.sh -n 5 apple uggs pencil water miley
