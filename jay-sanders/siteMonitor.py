import requests
from bs4 import BeautifulSoup
import time

def check():
    uri = raw_input("Enter the URI that you wish to check: ")
    sec = raw_input("Enter how many seconds long the interval is between "
    "checking for changes: ")
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(uri, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    
    init = str(soup)
    
    while True:
        response = requests.get(uri, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        if init == str(soup):
            time.sleep(float(sec))
            print("...")
        else:
            print("The website has changed!")
            break

check()
