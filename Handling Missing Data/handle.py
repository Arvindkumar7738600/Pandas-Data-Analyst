import pandas as pd

data = {
    "Name": ['Arvind', None, 'Ghanshyam', 'Ram', 'Krishna', 'Sita', 'Gita', 'Laxman', 'Bharat', 'Hanuman'],
    "Age": [10,20,30,40,50,60,70,None,90,100],
    "City": ['Ranchi','Mumbai', 'Delhi' ,None,'Bangalore','Chennai','Kolkata','Patna','Agra','Mathura'],
    "Salary" : [1000,2000,None,4000,5000,6000,7000,8000,9000,10000], 
    "Rating" : [1.1,2.2,None,4.4,5.5,6.6,7.7,8.8,9.9,10.0]
    }

df = pd. DataFrame(data)
print(df)

# .dropna() method to handle missing data by removing rows with missing values

#axis=0 drops rows with any missing values
#axis=1 drops columns with any missing values

df_cleaned = df.dropna(axis=0)
print("\nDataFrame after removing rows with missing values:")
print(df_cleaned)

