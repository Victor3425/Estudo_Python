import numpy as dsa

# Criando uma matriz
arr1 = dsa.array([[1,2,3],[4,5,6]])

print(type(arr1))
print(arr1)
print(arr1.shape)

#Criando uma matriz 2x3 apenas com número "1"
arr2 = dsa.ones((2,3))
print(arr2)

# Lista de listas
lista = [[13,81,22], [0,34,59],[21,48,94]]

# A função matrix cria uma matriz a partir de uma lista de listas
arr3 = dsa.matrix(lista)
print(type(arr3))
print(arr3)

# Formato da matriz 
print(dsa.shape(arr3))

# Tamanho da matriz
print(arr3.size)

# Tipo de dado
print(arr3.dtype)
