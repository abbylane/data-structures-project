//philo.cpp
//This contains the graph
#include <iostream>
#include <fstream>
#include <map>
#include <string>
#include <vector>
using namespace std; 

int main(){
    string word, prev_word;
    vector<string> marked;
    vector<string> heads; //first words inputed
    int count = 0; //keep track of # of words inputed (34 will be piped in per round)

    //graph is a map where key is word and value is list of its neighbors
    map<string, vector<string> > graph;

    prev_word = " ";

    while(cin >> word) {
	count++; //increment number of words inputed
	bool found = 0;

	cout << word << endl;

	//add word to graph
	if(prev_word != " ") {
	    graph[prev_word].push_back(word);
	} else {
	    heads.push_back(word);
	}
	prev_word = word;

	//check if it's in marked
	for(auto it1 = marked.begin(); it1 != marked.end(); it1++) {
	    if(*it1 == word) {
		found = 1;
		break;
	    }
	}
	if(found == 0) { //not already in marked
	    marked.push_back(word);
	} else {
	    cout << "\tInfinite loop can be entered." << endl; 
	    //ignore rest of input
	    for(int i = count; count < 34; count++) {
		cin >> word;
	    }
	    count = 0;
	    prev_word = " ";
	}
    }

    //remove the heads from the marked (so we can output formatting to file)
    for(auto mk = marked.begin(); mk != marked.end(); mk++) {
	for(auto hd = heads.begin(); hd != heads.end(); hd++) {
	    if(*mk == *hd) { //we found a head
		*mk = " ";
		break;
	    }
	}
    }

    //output to file
    ofstream outfile ("graph.dot");
    if(outfile.is_open()) {
	outfile << "digraph G {" << endl;
	//first, output formatting
	outfile << "{" << endl;
	//output heads
	for(auto it = heads.begin(); it != heads.end(); it++) {
	    outfile << *it << " [style=filled fontcolor=black fillcolor=darkolivegreen3]" << endl;
	}
	//output all other nodes
	for(auto mk1 = marked.begin(); mk1 != marked.end(); mk1++) {
	    if(*mk1 == " ") continue;
	    outfile << *mk1 << " [style=filled fontcolor=white fillcolor=gray40]" << endl;
	}
	outfile << "}" << endl;
	//output graph
	for(auto it2 = graph.begin(); it2 != graph.end(); it2++) {
	    for(auto it3 = it2->second.begin(); it3 != it2->second.end(); it3++) {
		outfile << it2->first << " -> " << *it3 << endl;
	    }
	}
	outfile << "}" << endl;
    }
    return 0;
}
