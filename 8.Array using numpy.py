#1.creating array using array()
from numpy import *
print("---Qustion 1 output using array()---")
a=array([1,2,3,4,5],int)
print(a)

a=array([1.1,2.2,3.3,4.4,5.5],float)
print(a)

a=array(['a','b','c','d','e'])
print(a)

a=array(['amar','bimal','ceema','dipak','rita'],dtype=str)
print(a)

#2.creating arrays using linspace
print("---Qustion 2 output using linspace---")
a=linspace(1,5,5)
print(a)

a=linspace(0,10,5)
print(a)


#3.creating arrays using logspace
print("---Qustion 3 output using logspace---")
a=logspace(1,5,5)
print(a)

#4.creaing array using arange()
print("---Qustion 4 output using arange()---")
a=arange(1, 10, 3)
print(a)

a=arange(10)
print(a)

a=arange(5, 10)
print(a)

#5.Creating Arrays using zeros() and ones()
print("---Qustion 5 output using zeros() and ones()---")
a=zeros(5)
print(a)

a=zeros(5, int)
print(a)

a=ones(5, float)
print(a)





