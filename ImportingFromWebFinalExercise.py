import requests
from bs4 import BeautifulSoup

#storing url
url = 'https://www.python.org/~guido/'

#get() method
r = requests.get(url)

#html text format:html_doc
html_doc = r.text

#converting to soup object
soup = BeautifulSoup(html_doc)

#showing the title
print(soup.title)

#showing the text
print(soup.get_text())

#showing all the hyper links
a_tag = soup.find_all('a')

for link in a_tag:
    print(link.get('href'))

