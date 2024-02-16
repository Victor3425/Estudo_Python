# Um array NumPy é uma estrutura de dados multimencional usada em computação cientifica e análise de dados. O NumPy fornece um objeto de matrizN- dimencional(ou ndarray),
# que é uma grande homogênea de elementos, geralmente números, que podem ser indexados por um conjunto de inteiros.

# Os arrays NumPy são mais eficientes do que as listas Python para armazenar e manipular grandes quantidades de dados, pois sçao implementados em Linguagem C e fornecem várias otmizações de desempenho.
# Além disso, o NumPy permite a fácil leitura e escrita de arquivos de dados, integração com outras bibliotecas Python e suporte a operações em paralelo usando várias CPUs ou GPUs.


import numpy as dsa

# Array criado a partir de uma lista Python

arrl = dsa.array([10,21,32,43,48,15,76,57,89])

print(arrl)

# Um objeto do tipo ndarray é um recipiente multidimencional de itens do mesmo tipo e tamanho
print(type(arrl))

# Verificar o formato do array
print(arrl.shape)