import pandas as pd
from urllib.request import urlretrieve

url = "https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv"

urlretrieve(url, 'winequality-red.csv')

df = pd.read_csv('winequality-red.csv',';')

print(df.head())