import requests
from bs4 import BeautifulSoup

#storing the url in variable
url = 'https://www.python.org/~guido/'

#packaging, sending and receiving the response
r = requests.get(url)

#storing the textual html in: html_doc
html_doc = r.text

#converting the html_doc to a beautifulsoup object
soup = BeautifulSoup(html_doc)

#applying the prettify function to indent the tags and make them more presentable
print(soup.prettify())