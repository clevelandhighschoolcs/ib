import urllib2
import time
import os
import sys

argument = str(sys.argv[1:])
urlToCapture = argument[2:len(argument)-2]

def capturePage(url):
	response = urllib2.urlopen(url)
	webContent = response.read()
	return webContent

def loop():
	
	timer = 0
	
	lastCapture = capturePage(urlToCapture)
	
	while True:
		
		content = capturePage(urlToCapture) #I know this takes times, so optimally I would add something to keep track of the difference, but nah.
		os.system('cls')
		print("Monitoring: " + urlToCapture + '\n')
		if lastCapture == content:
			print('There has been no change for ' + str(timer) + ' seconds.');
			for i in range(0, 5):
				print('- ')
				time.sleep(1)
			timer += 5
		else:
			print('THERE WAS A CHANGE WOW!')
			for i in range(0, 5):
				print('- ')
				time.sleep(1)
			timer = 0
			lastCapture = content		

loop()
