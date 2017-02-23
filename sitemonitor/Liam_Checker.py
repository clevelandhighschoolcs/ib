from urllib import urlopen
import time

my_url = 'http://rschlichting.weebly.com/hl-physics-3-4.html'

while True:
    str1 = urlopen(my_url).read()
    time.sleep(1)
    str2 = urlopen(my_url).read()

    if str1 == str2:
        print("...")

    else:
        print("Update!")
