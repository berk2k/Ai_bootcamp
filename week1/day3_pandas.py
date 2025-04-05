# series : 1D labeled arr capable of holding data of any type, and we have data frame
# data frame: 2D labeled ds like a table

import pandas as pd 
s = pd.Series([10,20,30], index=["a","b","c"])
print(s)

data = {"Name":["Alice","Bob"],"Age": [25,30]}

df = pd.DataFrame(data)
print(df)

df = pd.read_csv("data.csv")

#save
df.to_csv("data.csv",index=False) # additional index colm


# viewing data
print(df.head())
print(df.info())
print(df.describe())
print(df[["Name","Age"]])

print(df[df["Age"] > 25])
print(df.iloc[0])
print(df.iloc[:, 0])
print(df.loc[0])
print(df.loc[:,"Name"])
