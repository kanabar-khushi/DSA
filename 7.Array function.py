import array
print("---First method---")
a = array.array('i',[10,20,30,40,50])
for i in range(5):
    print(a[i])
    
print("---second method---")
import array as ar
a = ar.array('i',[60,70,80,90,100])
for i in range(5):
    print(a[i])
    
print("Third method")
from array import *
a = array('i',[1,2,3,4,5])
for i in range(5):
    print(a[i])

#1.append
print("---1.append output---")
a.append(6)
print("After append:", a)

#2.insert
print("---2.insert output---")
a.insert(1, 14)
print("After insert:", a)

#3.extend
print("---3.extend output---")
a.extend([7, 8, 8, 1])
print("After extend:", a)

#4.pop
print("---4.pop output---")
a.pop(1)
print("After pop:", a)

#5.remove
print("---5.remove output---")
a.remove(8)
print("After remove:", a)

#6.index
print("---6.index output---")
x = a.index(8)
print("Index of 8 is:", x)

#7.count
print("---7.count output---")
total = a.count(1)
print("Count of 1 is:", total)

#8.tolist
print("---8.tolist output---")
py_list = a.tolist()
print("As a Python list:", py_list)

#9.fromlist
print("---9.fromlist output---")
extra_list = [10, 20]
a.fromlist(extra_list)
print("After fromlist:", a)  

# 10. tostring()
print("---10.tostring output---")
a = array('i', [10, 20, 30])
print(a.tobytes())

# 11. fromstring()
print("---11.fromstring output---")
a = array('i', [10, 20, 30])
data = a.tobytes()
b = array('i')
b.frombytes(data)
print(b)

#12.reverse
print("---12.reverse output---")
a.reverse()
print("After reverse:", a)
