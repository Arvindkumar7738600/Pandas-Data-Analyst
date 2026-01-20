#There have two types of methods to read different file formats using pandas!!

# head() method and tail() method!!

#head means first 5 rows and tail means last 5 rows of the dataframe!!

import pandas as pd
df = pd.read_csv('customers-100.csv')
print('Displaying first 5 rows of the dataframe using head() method!!', df.head(5))

print('Displaying last 5 rows of the dataframe using tail() method!!', df.tail(5))