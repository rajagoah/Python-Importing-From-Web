import requests

#storing the url in a variable
url = 'http://www.datacamp.com/teach/documentation'

#packaging the request, sending the request and receiving the response
r = requests.get(url)

#reading the string format of the html
print(r.text)

