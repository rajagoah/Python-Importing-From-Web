import requests
from bs4 import BeautifulSoup

#storing the url in variable
url = 'https://www.python.org/~guido/'

#packaging, sending and receiving the request
r = requests.get(url)

#getting the html in text format
html_doc = r.text

#converting to beautifulsoup object
soup = BeautifulSoup(html_doc)

#getting the title
get_title = soup.title
print(get_title)

#getting the text
get_text = soup.get_text()
print(get_text)
