import pandas as pd

data = {
    "Name": ['Arvind', 'Shyam', 'Ghanshyam', 'Ram', 'Krishna', 'Sita', 'Gita', 'Laxman', 'Bharat', 'Hanuman'],
    "Age": [10,20,30,40,50,60,70,80,90,100],
    "City": ['Ranchi','Mumbai', 'Delhi' ,'Pune','Bangalore','Chennai','Kolkata','Patna','Agra','Mathura'],
    "Salary" : [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000], 
    "Rating" : [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0]
    }

df = pd. DataFrame(data)

#adding columns using assignment operator!!
#syntax: DataFrame['new_column'] = values
df['Bonus'] = [100,200,300,400,500,600,700,800,900,1000]
print("\n DataFrame after adding Bonus column:")
print(df)

# <---------------------------------------------------------------------> #

#adding columns using insert() method!!
#syntax: DataFrame.insert(loc, column, value, allow_duplicates=False)
df.insert(2, 'Experience', [1,2,3,4,5, 6,7,8,9,10])
print("\n DataFrame after adding Experience column at index 2:")
print(df)