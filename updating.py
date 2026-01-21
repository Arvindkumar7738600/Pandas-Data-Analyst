import pandas as pd

data = {
    "Name": ['Arvind', 'Shyam', 'Ghanshyam', 'Ram', 'Krishna', 'Sita', 'Gita', 'Laxman', 'Bharat', 'Hanuman'],
    "Age": [10,20,30,40,50,60,70,80,90,100],
    "City": ['Ranchi','Mumbai', 'Delhi' ,'Pune','Bangalore','Chennai','Kolkata','Patna','Agra','Mathura'],
    "Salary" : [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000], 
    "Rating" : [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0]
    }

df = pd. DataFrame(data)

#updating the dataframe by adding a new column 'Experience'!!
#syntax: df['new_column_name'] = values
df['Experience'] = [1,2,3,4,5,6,7,8,9,10]
print("DataFrame after adding new column 'Experience':")
print(df)




# .loc method to update specific values in the DataFrame!!
#syntax: df.loc[row_index, 'column_name'] = new_value
df.loc[2, 'City'] = 'New Delhi'  # updating city of the 3rd row (index 2)
df.loc[5, 'Salary'] = 6500       # updating salary of the
print("\n DataFrame after updating specific values:")
print(df)