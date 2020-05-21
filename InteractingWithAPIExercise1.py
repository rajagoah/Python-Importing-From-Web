import json

#opening the json file from the disc
with open('/Users/aakarsh.rajagopalan/Personal documents/Python projects/Data structure notes/Data pipeline Codes/data_file.json','r') as json_file:
    print(json.load(json_file))