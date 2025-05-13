#url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"

import pandas as pd 
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
# load data set

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# define features and target
features = df[['total_bill','size']]
target = df['tip']

print('features: \n', features.head())
print('target: \n', target.head())


X_train,X_test,y_train,y_test = train_test_split(features,target,test_size = 0.2, random_state=42)

print("training data set:",X_train.shape)
print("testing data set:",X_test.shape)

# visualize relationships
sns.pairplot(df,x_vars=["total_bill","size"],y_vars="tip",height=5,aspect=0.8,kind="scatter")
plt.title("feature vs target relationships")
plt.show()