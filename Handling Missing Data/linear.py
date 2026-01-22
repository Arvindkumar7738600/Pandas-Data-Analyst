import pandas as pd

data = {
    "Time": [1, 2, 3,4,51,],
    "Value": [10, None, 30, None, 50]
}


df = pd. DataFrame(data)
print( 'Before interpolation')
print(df)

df['Value'] = df['Value'].interpolate(method="linear")
print("after interpolation")
print(df)


#use of interpolate 

'''
1 - timer series data (example : stock market)
2 - Numeric data with trends
3 - avoid dropping row data rows 


'''