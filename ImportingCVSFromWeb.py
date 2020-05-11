import pandas as pd
from urllib.request import urlretrieve

#this code will load file from web and store them in local
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"
urlretrieve(url, 'winequality-red.csv')
df = pd.read_csv('winequality-red.csv',';')
print(df.head())

#this code will load file from web and convert to dataframe without saving the csv to local
url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-white.csv"
df = pd.read_csv(url,";")
print(df.head())
