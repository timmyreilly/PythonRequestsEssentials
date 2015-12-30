from bs4 import BeautifulSoup
import requests 
import json 
import time

soup = BeautifulSoup(open("scraping_example.html"), 'html.parser')

print soup.html.head.title 

print soup.prettify() 

for child in soup.html.children:
    print child.name 

print ".. div parent name .." 
print soup.div.parent.name 

for parent in soup.div.parents:
    print parent.name 

print soup.head.find_previous().name 
print soup.head.find_next().name 

print '.. doing replacements ..'

print soup.title.string 

soup.title.string = 'Web Scapping with Python Requests and BeautifulSoup by Balu'
 
print soup.title.string 

