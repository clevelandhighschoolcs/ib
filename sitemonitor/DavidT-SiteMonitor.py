import requests
from bs4 import BeautifulSoup
import time
import smtplib

while True:
	url = "http://Google.com/"
	headers = {'User-Agent': 'Mozilla/5.0 (Macinstosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers=headers) #Download Homepage
	soup = BeautifulSoup(response.text, "lxml") # Analyze site and grab all text

	if str(soup).find("Google") == -1:
		time.sleep(60)
		continue
	else:
		msg = 'Subject: ALERT CHANGE ON MAIN SITE, GO TO MOODLE'
		fromaddr = 'soreal@gmail.org'
		toaddrs = ['10/10myemail@gmail.org','notarealemail@gmail.com']
		
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		server.login("soreal.gmail.org", "passwo0rd")
		
		print('From: ' + fromaddr)
		print('To: ' + str(toaddrs))
		print('Message: ' + msg)
		
		server.sendmail(fromaddr, toaddrs, msg)
		server.quit()
		
		break