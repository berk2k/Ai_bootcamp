import matplotlib.pyplot as plt
import seaborn as sns 
import numpy as np
import pandas as pd

# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv

# load dataset
df = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

del df['species']
# calculate correlation matrix
correlation_matrix = df.corr()

# plot heatmap
sns.heatmap(correlation_matrix, annot=True,cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()