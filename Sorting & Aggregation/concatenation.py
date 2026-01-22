'''
we use for Vertically (row-wise)
horizonatally (column wise)
'''

#syntax: pd.concate([df1, df2, ....], axis = 0, ignore_index = True)

# vertically

import pandas as pd

df_region1 = pd.DataFrame({
    'CustomerID': [1, 2],
    'Name': ['Arru', 'Sweetiee']

})

#region 2

df_region2 = pd.DataFrame({
    'CustomerID': [3, 4],
    'Name': ['Arvind', 'Sweetiyaaa']

})

df_concate = pd.concat([df_region1, df_region2], axis=0, ignore_index=True)
print(df_concate)

#Horizantally
df_concate = pd.concat([df_region1, df_region2], axis=1, ignore_index=True)
print(df_concate)

