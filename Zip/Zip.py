# A função Zip() é uma função que agrupa elementos de múltuplas estruturas de dados iteráveis (como lista, tuplas ou outros objetos iteráveis) juntos em pares.
# A função zip() retorna um objeto zip, que pode ser convertido em outra estrutura de dados, como um lista ou dicionário, se necessário.

x = [1,2,3]
y = [4,5,6]

zip(x,y)

a = list(zip(x,y))
 
b = list(zip('ABCD','xy'))

d1= {'a':1,'b':2}

d2= {'c':4,'d':5}

# Zip vai unir as chaves
c = list(zip(d1,d2))

d = list(zip(d1, d2.values()))

def trocaValores (d1,d2):
    
    dicTemp = {}

    for d1key , d2val in zip(d1, d2.values()):
        dicTemp[d1key] = d2val

    return dicTemp    

e = trocaValores(d1,d2)

print(e)
