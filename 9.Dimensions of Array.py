# 1. Single dimensional array
from numpy import *

print("---Question 1 output 1D---")
arr1 = array([1, 2, 3, 4, 5],int32)
print(arr1)


# 2. Two dimensional array
print("---Question 2 output 2D---")
arr2 = array([[1, 2, 3], [4, 5, 6]],int32)
print(arr2)


# 3. Three dimensional array
print("---Question 3 output 3D---")
arr3 = array([[[1, 2, 3], [4, 5, 6]],[[1, 1, 1], [1, 0, 1]]],int32)
print(arr3)


# Attributes of an array

print("---ndim Attribute output---")
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

print("---shape Attribute output---")
print(arr1.shape)
print(arr2.shape)
print(arr3.shape)

print("---size Attribute output---")
print(arr1.size)
print(arr2.size)
print(arr3.size)

print("---itemsize Attribute output---")
print(arr1.itemsize)
print(arr2.itemsize)
print(arr3.itemsize)

print("---dtype Attribute output---")
print(arr1.dtype)
print(arr2.dtype)
print(arr3.dtype)

print("---nbytes Attribute output---")
print(arr1.nbytes)
print(arr2.nbytes)
print(arr3.nbytes)
