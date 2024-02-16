import numpy as dsa



arr1 = dsa.diag(dsa.arange(3))
#print(arr1)


d = arr1 = [1,1]
#print(d)

c = arr1 [1]
#print(c)

b = arr1 [:2]
#print(b)

arr2 = dsa.arange(10)
#print(arr2)

a = arr2[2:9:3]
#print(a)


e = dsa.array([1,2,3,4])
f = dsa.array([1,2,3,5])


if dsa.array_equal(e,f):
    print("Os arrys são iguais")

else:
    print("Os arrays são diferentes")    