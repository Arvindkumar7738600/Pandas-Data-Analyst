# using of info() method to get a concise summary of a DataFrame!!

import pandas as pd

df = pd.read_csv('customers-100.csv')

print('Displaying the information of the dataframe!!')
print(df.info())


# IN terminal display show objet. 
# objeact means string datatype in pandas.
# int64 means integer datatype in pandas.
# float64 means float datatype in pandas.


data = {
    "Name": ['Ram', 'Shyam', 'Ghanshyam' ],
    "Age": [10,20,30],
    "City": ['Nagpur','Mumbai', 'Delhi']
    }
df = pd. DataFrame(data)
print('Displaying the information of the dataframe!!')
print(df.info())
