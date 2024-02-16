import numpy as dsa

# Lista de listas
lista = [[13,81,22], [0,34,59],[21,48,94]]

# A função matrix cria uma matriz a partir de uma lista de listas
arr1 = dsa.matrix(lista)

print(arr1)

# Indexação da matriz
print(arr1[2,1])

# Indexação da matriz 
print(arr1[0:2,2])

# Indexação da matriz 
print(arr1[1,])

# Alterando um elemento da matriz
arr1[1,0] = 100
print(arr1)

x = dsa.array([1,2]) # NumPy decide o tipo dos dado 
y = dsa.array([1.0,2.0]) # NumPy decide o tipo dos dado
z  = dsa.array([1,2], dtype = dsa.float64) # Forçamos um tipo de dado em particular

print(x.dtype, y.dtype, z.dtype)

arr2 = dsa.array([[24, 76, 92, 14], [47, 35, 89, 2]], dtype = float)
print(arr2)

# O itemsize de um array numpy é um atributo que retorna o tamanho em bytes de cada elemento do array. 
# Em outras palavras, o itemsize representa o número de bytes necessários para armarzenar cada valor do array numpy.

print(arr2.itemsize)
print(arr2.nbytes)
print(arr2.ndim)