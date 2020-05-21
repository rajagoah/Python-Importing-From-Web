import pandas as pd

#storing the url in the variable url
url = 'http://s3.amazonaws.com/assets.datacamp.com/course/importing_data_into_r/latitude.xls'

#reading the excel sheet into the xls dictionary
xls = pd.read_excel(url, sheet_name = None)

#displaying the names of the sheet. xls is dictionary, with the sheet names as the key
print(xls.keys())

#dipslaying the head of the first sheet
print(xls['1700'].head())