## Data Structures Spring 2018 Final Project: Wikipedia Trick

This is the gitlab repository for our final data structures project. 
We utilized python, C++ and the MacPorts graphviz library to graphically represent the path 
taken by opening the first non-bolded, non-italicized link in consecutive 
Wikipedia pages, until a loop was reached. 

### Setup 

Unfortunately, our project can only be run on machines with Mac OS X. Before running, users must install Xcode and MacPorts on their machine. Instructions to do that are at "Chapter 2" on [this site](https://guide.macports.org/#installing.xcode). Once MacPorts is installed, the user must run the following commands to install the ports used for this project: 

`sudo port install graphviz `
`sudo port install graphviz-gui `

We linked the various parts of our project in one shell script "run.sh". This script can be run on the command line with `./run.sh -n (# of keywords) (Keywords separated by spaces) `

It will save a file called graph.dot.png to the same directory where you ran the script which contains a visual representation of the pages visted. 

## Files: 

#### Makefile
Compiles philo.cpp and tests program against sample plain text output. 

#### crawl.py
Uses Python request capabilities to get code from user requested Wikipedia page. Parses HTML for first link and opens link. Recrusively opens links on each consecutive page until a loop is reached in pages (one page is leading to the same cycle of page openings) 

#### output1, output3, output5
Expected output of program for set keywords to crawl. 

#### philo.cpp
Takes in output from crawl.py and pushes traversed pages into a map, where the key is the word and the value is its list of neighbors. Outputs the correct formatted list to a "graph.dot" file so that a visual graphic may be created.  

#### run.sh
Combines Python and C++ progams, and creates a png from .dot file. 

### Members
Abby Lane (alane3, Section 01)

Abigail Mrenna (amrenna, Section 02)

Margaret West (mwest6, Section02)

## Contributions

Abby Lane:
1. Creation of functions in crawl.py
2. creation of Makefile 
3. creation of run.sh
4. benchmarking

Margaret West:
1. Planning overall strategy and design choices for each part of the project  
1. work on crawl.py, especially with HTML parsing 
2. Research on use of Graphviz 
3. work on philo.cpp, especially with formatting output

Abigail Mrenna:

1. creation of philo.cpp 
2. general debugging 
3. benchmarking 
4. Extensive help manually checking correctness of crawl.py 


## Demonstration Video 
https://drive.google.com/file/d/1WDw_X9t3u2Yc6kWg7fqUwTKvOFlBHJPW/view?usp=sharing

## Presentation Slides
https://docs.google.com/presentation/d/1ESmDPcPllamQNsFswE3y96GqDRV6hgMkoI5nBZmALfY/edit?usp=sharing
