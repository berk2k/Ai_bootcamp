# clean data by handling missing values
import pandas as pd 
import numpy as np 

# create a dataset

data = {
    "Name":["Alice","Bob",np.nan,"David"],
    "Age":[25,np.nan,30,35],
    "Score":[85,90,np.nan,88]
}

df = pd.DataFrame(data) 

print("original dataset: \n",df)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Score"] = df["Score"].interpolate()


df = df.rename(columns={"Name":"Student_Name","Score":"Exam:Score"})
 