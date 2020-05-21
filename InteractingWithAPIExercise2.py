import requests
from bs4 import BeautifulSoup

#storing url. the api key is mentioned after '?' followed by the query string for retrieving information about the movie, the social network
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

#using the get() method in the requests module
r = requests.get(url)

#converting to soup object
text = r.text
soup = BeautifulSoup(text)

#printing the response
print(soup.prettify())