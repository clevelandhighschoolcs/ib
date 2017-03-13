import requests
from bs4 import BeautifulSoup
import time
import difflib

def main():
	#url = "http://"+str(input("URI to monitor: "))
	url = "http://rschlichting.weebly.com/hl-physics-3-4.html"
	updateDelay = int(input("Time to wait before each update:"))

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, "lxml")

	while True:
		time.sleep(updateDelay)
		print("Checking "+url+"...")
		newResponse = requests.get(url, headers=headers)
		newSoup = BeautifulSoup(newResponse.text, "lxml")
		d = difflib.Differ()
		diff = d.compare(str(soup), str(newSoup))
		print("Changes found.")
		#print("".join(diff))

if __name__ == "__main__":
	main()
