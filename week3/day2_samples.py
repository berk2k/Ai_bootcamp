import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import norm,binom,poisson,uniform 

# gaussian distribution 
x = np.linspace(-4,4,100)
plt.plot(x,norm.pdf(x,loc=0,scale=1),label="gaussian(u=0,s=1)")

# binomial distribution

n,p = 10,0.5
x = np.arange(0,n+1)
plt.bar(x,binom.pmf(x,n,p),alpha=0.7,label="binomial(n=10,p=0.5)")

#poisson dist

lam = 3
x = np.arange(0,10)
plt.bar(x,poisson.pmf(x,lam),alpha=0.7,label="poisson(l=3)")

#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

from scipy.stats import skew,kurtosis
import pandas as pd 
import seaborn as sns

# load dataset 
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# analyse sepal_length
feature = df["sepal_length"]
print("skewness: ",skew(feature))
print("kurtosis: ",kurtosis(feature))

#visualize dist
sns.heatplot(feature,kde=True)
plt.show()


