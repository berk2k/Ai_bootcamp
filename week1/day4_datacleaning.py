
# data transformation
df = df.rename(columns={"old_name":"new_name"})

df["column_name"] = df["columns_name"].astype("float")
df["column_name"] = pd.to_datetime(df["column_name"])

df["new_column"] = df["existing_column"] * 2

# combining and merging dataframes
combined = pd.concat([df1,df2],axis=0)
combined = pd.concat([df1,df2],axis=1)

merged = pd.merge(df1,df2,on="common_column")
merged = pd.merge(df1,df2,how="left",on="common_column")
merged = pd.merge(df1,df2,how="inner",on="common_column")

joined = df1.join(df2,how="inner")







df = df.dropna()
df = df.dropna(axi=1)

df["column_name"] = df["column_name"].fillna(0)

df.fillna(method="ffill")
df.fillna(method="bfill")

df["column_name"] = df["column_name"].interpolate()


