import matplotlib.pyplot as plt

import seaborn as sns 
import numpy as np

data = np.random.rand(5,5)
""" sns.heatmap(data,annot=True,cmap="coolwarm")
plt.title("Heatmap") """
sns.pairplot(df)

plt.show()

# basic plot
""" x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y)
plt.show() """

# Line plot

""" plt.plot([1,2,3],[10,20,30], label = "trend",linestyle="--",marker="o")
plt.title("line plot")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show() """

# Bar chart
""" categories = ["A","B","C"]
values = [10,15,7]
plt.bar(categories,values,color="blue")
plt.title("Bar chart")
plt.show() """

# Histogram
""" data = [1,2,2,3,3,3,4,4,4,4]
plt.hist(data, bins=4,color="green",edgecolor="black")
plt.title("Histogram")
plt.show() """

# Scatter plot
""" x = [1,2,3,4,5]
y = [10,12,25,30,45]
plt.scatter(x,y,color="red")
plt.title("Scatter plot")
plt.legend(["Dataset1"])
plt.show() """
