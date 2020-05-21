import requests
from bs4 import BeautifulSoup

#storing url in variable
url = 'https://www.python.org/~guido/'

#packaging, sending and receiving the response
r = requests.get(url)

#html_doc storing the html in text
html_doc = r.text

#converting to beauitfulsoup object
soup = BeautifulSoup(html_doc)

#finding all the tags 'a' to idenitfy the urls in hyperlinks
a_tags = soup.find_all('a')

#enumerating over the a_tags variable to extract the links within the href tag
for link in a_tags:
    print(link.get('href'))