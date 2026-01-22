#sorting means manage data by own!!

#Syntax: df.sort_values(by='column Name', True/False) = inplace = True)

import pandas as pd

data = {
    "Name": ["Arru", "Kumar", "Sweetiyaa"],
    "Age": [18, 20, 17],
    "salary": [150000, 100000, 200000]
    }

df = pd.DataFrame(data)
df.sort_values(by="Age", ascending=True, inplace=True)
print(df)
