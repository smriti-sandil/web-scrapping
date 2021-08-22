""" If you want to scrap website
1 use the  API
2. HTML scaping using some tool like bs4
-- Install  all requirements
pip install html5lib
pip install bs4
pip install requests

"""
from os import link
import requests
from bs4 import BeautifulSoup
url= "https://codewithharry.com"
#step-1  Get the HTML
r=requests.get(url)
htmlcontent=r.content
# print(htmlcontent)

# step-2 Parse the HTML

soup=BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)

# step-3 HTML The traversal
# Types of objects
# 4 . Comment


# title= soup.title    #3. BeautifulSoup
# print(type(title))   #bs4.element.Tag # 1 Tag
# print(type(soup)) 
# print(type(title.string)) # 2. NavigableString

# Get the title of Html page
title= soup.title 
# Get all the paragraph from the page
paras=soup.find_all('p')
# print(paras)

# get all the anchor tags from the page
anchors=soup.find_all('a')


# print(anchors)
print(soup.find('p'))  #get first element  in the html page

print(soup.find('p')['class']) #get classes of any elements in the html page
all_links=set()
# find all the elements with class lead
print(soup.find_all('p',class_='lead'))

print(soup.find('p').get_text())

print(soup.get_text())

#  Get all the links on the page:
for link in anchors:
    print(link.get('href'))


# 4. Comment
markup='<p><!-- this is comment --></p>'



