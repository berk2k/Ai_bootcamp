import numpy as np
# broadcasting operations 
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
vector = np.array([1,0,-1])

result_add = matrix + vector
print("add: ",result_add)

result_mul = matrix * 2
print("multiplication: ", result_mul)

#generate and filter a random dataset
dataset = np.random.randint(1,51,size=(5,5))
print("original: \n", dataset)

# filter values > 25 and replace with 0
dataset[dataset > 25] = 0
print("modified dataset: \n",dataset)

# calculate summary stats
print("sum: ", np.sum(dataset))
print("mean: ",np.mean(dataset))
print("std:",np.std(dataset))