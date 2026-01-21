import pandas as pd

data = {
    "Name": ['Arvind', 'Shyam', 'Ghanshyam', 'Ram', 'Krishna', 'Sita', 'Gita', 'Laxman', 'Bharat', 'Hanuman'],
    "Age": [10,20,30,40,50,60,70,80,90,100],
    "City": ['Ranchi','Mumbai', 'Delhi' ,'Pune','Bangalore','Chennai','Kolkata','Patna','Agra','Mathura'],
    "Salary" : [1000,2000,3000,4000,5000,6000,7000,8000,9000,10000], 
    "Rating" : [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10.0]
    }

df = pd. DataFrame(data)

#filtred in single condition!!
high_salary = df[df['Salary'] > 5000]
print("Rows with Salary greater than 5000:")
print(high_salary)


#filtered in multiple conditions!!
filtered_data = df[(df['Age'] > 30) & (df['Rating'] < 8.0)]
print("\nRows with Age greater than 30 and Rating less than 8.0:")
print(filtered_data)


#filtered using OR condition!!
filtered_or = df[(df['City'] == 'Mumbai') | (df['City']== 'Delhi')]
print("\nRows where City is either Mumbai or Delhi:")
print(filtered_or)