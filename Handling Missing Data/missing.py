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

#missing data handling!!

#True if there are any missing values in the DataFrame
#False if there are no missing values

print(df.isnull())  # Check for missing values

print(df.isnull().sum())  # Count of missing values in each column