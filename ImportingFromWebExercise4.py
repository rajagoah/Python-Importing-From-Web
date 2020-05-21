from urllib.request import urlopen, Request

#storing the url in the url variable
url = 'http://www.datacamp.com/teach/documentation'

#packaging the request
request = Request(url)

#sending the request and catching the response
response = urlopen(request)

#reading the http response
print(response.read())