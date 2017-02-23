import requests # downloading them pages
from bs4 import BeautifulSoup # to parse downloads
import time # Control when program should run
import smtplib # mailing service!

Hello = True
World = False

url = "https://thimbleprojects.org/breadpuffs/102045" # site you wish to extract html code from
headers = {'User-Agent': 'Chrome/39.0.2171.95'} 
response = requests.get(url, headers=headers) # getting that code
original = BeautifulSoup(response.text, "html.parser") # parsing into html 
check = BeautifulSoup(response.text, "html.parser")
	
while True:
	if str(original) == str(check): # checks if html strings matches
		if Hello == True: 
			print "It's all clear Captain."
		if World == True:
			print "No dangers here Captain."
		response = requests.get(url, headers=headers)
		check = BeautifulSoup(response.text, "html.parser") # "check" becomes whatever html code the site has now
		if Hello == False:
			Hello = True
			World = False
		else:
			World = True
			Hello = False
		time.sleep(4)
	
	else: #if html strings do not match, as in, changes in the code, send email
		print check
		server = smtplib.SMTP('smtp.gmail.com', 587) # I DON'T KNOW WHAT ALL THIS STUFF IS
		server.ehlo()
		server.starttls()
		server.login("MyEmail@helloworld.com","mypassword") # username and password here

		SUPERSECRETMESSAGE = "The space and time continuum is collapsing Captain." # message content
		FROM = "MyEmail@helloworld.com" # your email
		TO = "SomeOtherEmail@helloworld.com" # whoever you're sending it to
		
		server.sendmail(FROM, TO, SUPERSECRETMESSAGE) # the email is sent~
		server.quit()
		print "A letter has arrived Captain."
		time.sleep(10)
		break
