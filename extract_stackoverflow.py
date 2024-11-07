import urllib.request 
from bs4 import BeautifulSoup
import requests
import re

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
url = "http://stackoverflow.com/?tab=month"
headers={'User-Agent':user_agent,} 

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
html = response.read()

soup = BeautifulSoup(html, 'html.parser')
soup2  = soup.text
lines = soup2.splitlines()
with open("/Users/priyatham/prasanna/Python/output_file.txt",'w') as file_out: 
    file_out.write(lines)
title = soup.title.string

print (f'title of the webpage: {title}')