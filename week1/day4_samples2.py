import pandas as pd 
import numpy as np 

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["Alice","Bob","Charlie"],
    "Age":[25,30,35],
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Score":[80,85,90]

}) 

merged = pd.merge(df1,df2,how="inner",on="ID")
print("merged dataset: \n", merged)

merged["Score_Percentage"] = (merged["Score"] / 100) * 100
print("Transformed dataset \n", merged)