#!/usr/bin/python
'''
  Unfortunately, since rondaniel.com uses crappy illegal HTML,
we need a library/module called BeautifulSoup.  It makes parsing
HTML/XML super easy.  It's not installed by default, but you can
pip install it.  Here's a batch file that will install it:

---------------------------------------------------------------------------------

@echo off
powershell -NoProfile -ExecutionPolicy unrestricted -Command "iex ((new-object net.webclient).DownloadString('https://chocolatey.org/install.ps1'))" && SET PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin
call cinst pip
cal pip install BeautifulSoup
timeout /t 10
@echo on

---------------------------------------------------------------------------------

  Also, I added a method to grab the html just for convenience.
fetchHTML() will grab the html from a link and filterForAudio()
will return a list of all mp3s as a list from inside a tag like:

...
<a href="file1.mp3"></a>
<a href="file2.mp3"></a>
<a href="file3.mp3"></a>
...

as:

["file3.mp1","file2.mp3","file3.mp3"]

'''

import urllib2								# Needed for fetchHTML
from BeautifulSoup import BeautifulSoup		# filterForAudio

def pause():
	raw_input("")
## Takes in a url string and outputs html string
def fetchHTML(link):					# This defines the method/function
	response = urllib2.urlopen(link)	# Opens the webpage
	html = response.read()				# Reads the data on the page
	return(html)						# Returns the html as a string


## Takes in the page html and optionally the root url (needed for the full mp3 path)
def filterForAudio(html,url=""):												# Defines the method/function
	soup = BeautifulSoup(html)													# Loads the html as a BS object
	links = soup.findAll('a', href=True)										# Finds all of the <a> tags
	mp3s = []																	# Creates an empty list that we can put the paths into
	for l in links:																# Iterates through the links
		if l['href'].endswith('.mp3'):											# Checks to see if the href="" part ends with .mp3
			try:																# Will try to build a link using the supplied root link
				mp3 = "%s%s"%(url.replace((url.split("/")[-1]),""),l['href'])	# This may look ugly, but I wanted to do it as a one-liner.  It basically just builds the link cleanly
			except:																# In case there is a problem with the line above, it will build a relative link
				mp3 = l['href']													# Diddo ^
			mp3s.append(mp3)													# Adds the newly built link to the mp3 list
	return(list(set(mp3s)))														# Returns a unique list

'''
link = 'http://www.rondaniel.com/library/14-2Chronicles/2Chronicles.html'	# Specifies the root url
link = 'http://cityviewonline.org/sounds/event/event.htm'					# CityView Example
html = fetchHTML(link)														# Uses the method that we built above to get the html from the root url
mp3s = filterForAudio(html,link)											# Uses the method that we built above to return a list of mp3 urls

for i in mp3s:		# Loops through the mp3s list
	print i			# Prints the link
raw_input("Done")	# "Pauses" the script
'''
links = ["http://www.rondaniel.com/library/14-2Chronicles/2Chronicles.html","http://cityviewonline.org/sounds/event/event.htm"]
for link in links:
	html = fetchHTML(link)
	mp3l = filterForAudio(html)
	for  in mp3l
	print 







pause()



