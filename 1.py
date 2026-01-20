# How to read different file formats using pandas!!

import pandas as pd

#read the CSV file into a DataFrame!!

df = pd.read_csv('customers-100.csv')

#excel sheet style display syntax!!

df = pd.read_excel('customers-100.xlsx')

#json file read syntax!!

df = pd.read_json('customers-100.json')


print(df)