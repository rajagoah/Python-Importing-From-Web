import pandas as pd

df = pd.read_csv('/Users/aakarsh.rajagopalan/Personal documents/Datasets for tableau/Tableau project dataset/Foreign_Exchange_Rates.csv')

print(df[:0])

print(df[['Time Serie','INDIA - INDIAN RUPEE/US$']])