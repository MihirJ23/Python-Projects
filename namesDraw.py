import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup

#here is the problem
#Scraping Numbers from HTML using BeautifulSoup 
#In this assignment you will write a Python program similar to http: // www.py4e.com/code3/urllink2.py. 
#The program will use urllib to read the HTML from the data files below, 
#and parse the data, extracting numbers and compute the sum of the numbers in the file.

url = 'http://python-data.dr-chuck.net/known_by_Aimie.html'
count = int(input('Enter count:'))
position = int(input('Enter position:'))-1
html = urllib.request.urlopen(url).read()

names = BeautifulSoup(html,"html.parser")
href = names('a')

for i in range(count):
    link = href[position].get('href', None)
    print(href[position].contents[0])
    html = urllib.request.urlopen(link).read()
    names = BeautifulSoup(html,"html.parser")
    href = names('a')
