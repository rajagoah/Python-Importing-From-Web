#importing relevant packages
from urllib.request import urlopen, Request

#storing the url in a variable
url = "https://www.datacamp.com/teach/documentation"

request = Request(url)

response = urlopen(request)

print(type(response))
