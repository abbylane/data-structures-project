#!/usr/bin/env python3

import sys
import os
import signal
import re
import requests
from bs4 import BeautifulSoup as BS
# from IPython.display import HTML

URL = 'http://en.wikipedia.org/w/api.php'
BASE = 'http://en.wikipedia.org'
num = 1

def usage(status=0): # __________________________________________________________
	print('''Usage: ./{} SEARCH
		-n NUM number of keywords to crawl
	Search for wikipedia page of SEARCH. Crawl first non-bolded, non-italicized link on each
	page until loop is reached'''.format(os.path.basename(sys.argv[0])))
	sys.exit(status)
# __________________________________________________________

def signal_handler(signal, frame):
	print("\n\n____________________________Received CTRL-C signal____________________________\n")
	sys.exit(0)

# __________________________________________________________

def wikipedia(query):
	'''Search Wikipedia for key, get link of page'''# if query is empty, do nothing
	if not query:
		return

	# request wikipedia search results
	params = {'action': 'query', 'list': 'search', 'format': 'json', 'srsearch': query}
	response = requests.get(URL, params=params) 

	# check that search was successful
	if response.status_code != 200:
		print ('Error: could not retrieve search for {}'.format(query))
		return

	data = response.json()
	title = data['query']['search'][0]['title'] # get article title

	return(title) # return article title of first result 
# __________________________________________________________

def philo(URL):
	''' OPEN ALL ZE LINKS '''

	r = requests.get(URL)
	try: 
		lines = r.text.splitlines()
	except: 
		print("could not splitlines")

	bodycheck = 0;
	tablecheck = 0;
	divcheck = 0; 
	for line in lines:
		if line == '<h2>Contents</h2>':
			divcheck = 3
		if '<body' in line:
			bodycheck = 1;
		if '<table' in line:
			tablecheck += 1;
		if '</table>' in line:
			tablecheck -= 1;
		if '</div>' in line and divcheck > 0:
			divcheck -=1 
			#print (line)
			# parse for first line with 'href=', bold, doesn't include key formatting words such as 'align' or '<small>'
		if bodycheck==1 and tablecheck==0 and divcheck ==0 and 'href=' in line and '<table' not in line:
			if '<p>' in line or '<li' in line: 
				ref = line
				break

	l = ref.split() # split first line
	italcheck = 0;
	parencheck = 0; 
	for word in l:
		if '<i' in word:
			italcheck += 1
		if '</i>' in word:
			italcheck -= 1
		if '(' in word:
			parencheck += 1
		if ')' in word:
			parencheck -= 1; 
		if word == '<p><b>Thought</b>':
			link = '/wiki/Lingustics'
		if word == '<p><b>Wikipedia</b>': 
			link = '/wiki/Encyclopedia'
		# get instances of href
		if italcheck==0 and parencheck==0 and'href=' in word and '</sup>' not in word and '</sub>' not in word:
			link = word
			break

	'''for word in l: 
		if 'title' in word:
			nextPage = re.findall(r ' "(.*?)" ', word)
			#nextPage = word
			nextPage = word
			tempList = nextPage.split("\"")
			nextPage = tempList[1]
			break'''
	'''r = r'title=\".*\"'
	for word in l:
		if 'href' in word:
			print("href: ", word)
			break'''
	
	link = link.replace("\"", "")
	link = link.replace("href=","")
	title = link.replace("/wiki/", "")
	title = title.replace("-", "_")
	title = title.replace(":", "_")
	title = title.replace("/", "_")
	title = title.replace("(", "") # remove ()
	title = title.replace(")", "")

#	title = title.replace("_", " ")

#	print("\"{}\"".format(title))
	print(title)
	#print("{}".format(nextPage))
	return (BASE + link)


#   parse command line options_____________-

if len(sys.argv) == 1:
	usage(1)
elif sys.argv[1] == '-h':
	usage(0)
elif sys.argv[1] == '-n':
	n = sys.argv[2] 		# default n = 1 keyword
	search = sys.argv[3:] 	# list of keywords to search
else: 
	search = sys.argv[1:]


# main execution
if __name__ == '__main__':
	signal.signal(signal.SIGINT, signal_handler)
	traversed = [] # sites traversed

	for index, keyword in enumerate(search):
		keyword = keyword.replace("-", "_")
		keyword = keyword.replace(" ", "_")
		keyword = keyword.replace(":", "_")
		keyword = keyword.replace("/", "_")
		print(keyword)
		# first search from stdin
		#print(index + 1, '. Initial Search: \t{}'.format(keyword))
		title = wikipedia(keyword) #returns title of page assoc w keyword
	#	title = title.replace(' ', '_') 
		#print("title: {}".format(title)) #TODO: remove later

		traversed.append(title)
		HREF = ('http://en.wikipedia.org/wiki/{}'.format(title))
		#print('Initial Link: \t\t{}'.format(HREF))

		link = philo(HREF)

		MAX   = 32

		count = 0
		while count < MAX:
			link = philo(link)
			count = count + 1
		print("")
