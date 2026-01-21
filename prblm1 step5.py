import pandas as pd

data = {
    "Name": ['Arvind', 'Shyam', 'Ghanshyam', 'Ram', 'Krishna', 'Sita', 'Gita', 'Laxman', 'Bharat', 'Hanuman'],
    "Age": [10,20,30,40,50,60,70,80,90,100],
    "City": ['Ranchi','Mumbai', 'Delhi' ,'Pune','Bangalore','Chennai','Kolkata','Patna','Agra','Mathura'],
    "Salary" : [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000], 
    "Rating" : [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0]
    }

df = pd. DataFrame(data)

#displaying the dataframe !!

print("sample dataframe is :")
print(df)

print("Names (single column return dataseries)")
print(df['Name'])  #1st way to access a single column

# selecting multiple columns!!

subset = df[['Name','City']] #2nd way to access multiple columns
print("\n Selecting multiple columns!!")
print(subset)