import requests

#storing the url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'

#package the request and store the response
r = requests.get(url)

#converting to json
json_data = r.json()

#enumerating
for key in json_data.keys():
    print(key,' : ',json_data[key])