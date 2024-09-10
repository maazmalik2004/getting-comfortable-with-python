import numpy as np
import pandas as pd

arr = np.array([1,2,3,4])
print(arr*2)

data = {'name':['john','anna'],'age':[30,25]}
df = pd.DataFrame(data)
print(df)

arr2d = np.array([[1,2],[3,4],[5,6]])
print(arr2d*2)

arr_3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr_3d)

print(arr2d.shape)
print(arr2d.size)

#initializing special arrays
zeros = np.zeros((2,3))#we pass a tuple
print(zeros)

ones = np.ones((3,3))#we pass a tuple
print(ones)

random = np.random.rand(2,3)#we pass dimensions directly
print(random)

#performing operation on array means we can perform the same operation on each element of the array
print(arr+2)
print(arr*3)
print(arr/2)

#slicing and indexing
arr = np.array([10,20,30,40,50])
print(arr[:3])#cuts the first three element from 0 included to 3 index excluded

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[1,:])#accessing second row
print(arr2d[:,2])#accessing third column

#cropping an array
print(arr2d[0:2,1:3])

arr1 = np.array([1,2,3])
arr2 = np.array([[1],[2],[3]])
result = arr1+arr2
print(result)

arr = np.array([1,2,3,4,5,6])
reshapedArr = arr.reshape((2,3))
print(reshapedArr)

#dot operation = matrix multiplication
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
dotArr = np.dot(mat1,mat2)
print(dotArr)

#boolean masking
arr = np.array([10, 20, 30, 40, 50])
result = [int(arr[x]) for x in range(5) if arr[x] > 25]
print(result)

arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))
print(np.mean(arr))
print(np.var(arr))

print(type(arr))
