#syntax: pd.merg(df1, df2, on = 'column_name', how = 'type of data')

# df1 means dataseta 1



import pandas as pd 

df_data = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'Name': ["sweetiee", "Arru", "Arviind"]

})

#order data file:
df_order = pd.DataFrame({
    'Customer_ID': [1, 2, 3],
    'OrderdAmount': [1000, 2000, 3000]
})

#merge

df_merge = pd.merge(df_data, df_order, on = "Customer_ID", how = 'inner')
print('inner join')
print(df_merge)