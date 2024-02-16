import numpy as dsa


# O método flatten() com NumPy é usado para criar uma cópia unidimensional(ou "achatada") de um array multimencional. 
# Isso significa que o método cria um novo array unidimensional, que contém todos os elementos array mutimencional original, mas que está organizado em uma única linha.
# A ordem dos elementos no novo array unimendisional segue a ordem dos elementos no array multidimensional original. 


arr1 = dsa.array([[1,2,3,4],[5,6,7,8]])
print(arr1)

# 'Achatando' a  matriz
arr2 = arr1.flatten()
print(arr2)

arr3 = dsa.array([1,2,3])
print(arr3)

# Repetindo os elementos de um array
a= dsa.repeat(arr3,3)
print(a)

# Repetindo os elementos de um array
b = dsa.tile(arr3,3)
print(b)

arr4  = dsa.array([5,6])

c = dsa.copy(arr4)
print(c)