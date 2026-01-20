import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)



'''how to save dataframe into different file formats using pandas!!'''

# CSV file format!!

df.to_csv('output_data.csv', index=False) #indexed parameter is used to avoid writing row numbers.


#Excel file format!!
'''How to save dataframe into excel file format!!'''

df.to_excel('output_data.xlsx', index=False)



#JSON file format !!

'''How to save dataframe into json file format!!'''

df.to_json('output_data.json')

