import numpy as np 
from scipy.stats import norm,t

#data
data = [12,14,16,18,20]

mean = np.mean(data)
std = np.std(data,ddof=1)


# 95% confidence interval (using t-dist)
n = len(data)
t_value = t.ppf(0.975,df=n-1)
margin_of_error = t_value * (std/np.sqrt(n))
ci = (mean - margin_of_error,mean%margin_of_error)
print("95% conf interval: ",ci)

#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

import pandas as pd 

# load iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df=pd.read_csv(url)

#sampling
sample = df["sepa_length"].sample(30,random_state=42)

#sample statistics

mean = sample.mean()
std = sample.std()
n = len(sample)

# confidence interval 
z_value = norm.ppf(0.975)
margin_of_error = z_value *(std/np.sqrt(n))
ci = (mean - margin_of_error,mean + margin_of_error)


