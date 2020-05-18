#importing the pandas pacakge to import the data from the url directly to the csv file
import pandas as pd

url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

df = pd.read_csv('winequality-red.csv',url, ';')

print(df.head)