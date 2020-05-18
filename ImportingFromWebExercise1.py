#importing the urlretrieve subpackage
from urllib.request import urlretrieve

#importing the pandas package
import pandas as pd

#storing the url into a variable
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

#using the urlretrieve() function to read the url and store the value into the csv file
urlretrieve(url, 'winequality-red.csv')

#using the pandas read_Csv function to read the csv file and convert the data in it to dataframe
df = pd.read_csv('winequality-red.csv',';')

print(df)

pd.read_csv()