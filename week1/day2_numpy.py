import numpy as np

# array and scalar broadcasting

arr = np.array([1,2,3])
print(arr + 10)

matrix = np.array([[1,2,3],[4,5,6]])
vector = np.array([1,0,1])
print(matrix + vector)

# Aggregation Functions : compute summary statistics for arrays

arr = np.array([[1,2,3],[4,5,6]])
print("sum: ", np.sum(arr))
print("mean: ", np.mean(arr))
print("max: ", np.max(arr))
print("std: ", np.std(arr))
print("sum along rows: ", np.sum(arr,axis=1))
print("sum along cols: ", np.sum(arr,axis=0))

# Boolean Indexing and filtering

arr = np.array([1,2,3,4,5,6])
evens = arr[arr % 2 == 0]

# random number generation and setting seeds
np.random.seed(42)

random_array = np.random.rand(3, 3)
print("random array: \n", random_array)

random_integers = np.random.randint(0,10,size=(2,3))
print("random integers: \n", random_integers)



