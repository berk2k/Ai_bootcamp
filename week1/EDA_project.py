# EDA STEPS
# Data cleaning,data transformation,aggregation and filtering
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns

# load titanic ds
url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# inspect data
print(df.info())
print(df.describe())

# handle missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# remove duplicates
df = df.drop_duplicates()

# filter data: passengers in first class
first_class = df[df["Pclass"] == 1]
print("First Class Passengers: \n",first_class.head())

# bar chart: survival rate by class

survival_by_class = df.groupby("Pclass")["Survived"].mean()
survival_by_class.plot(kind="bar",color="skyblue")
plt.title("Survival Rate by class")
plt.ylabel("Survival Rate")
plt.show()

# histogram: age distribution
sns.histplot(df["Age"],kde=True,bins=20,color="purple")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# scatter plot: age vs fare
plt.scatter(df["Age"],df["Fare"],alpha=0.5,color="green")
plt.title("Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show() 

