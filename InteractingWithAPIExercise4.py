import requests

#storing url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

#getting the respose
r = requests.get(url)

#encoding to json
json_data = r.json()

#printing
for i in json_data.keys():
    print(i)
    print(json_data['query'])