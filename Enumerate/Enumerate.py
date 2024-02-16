# A função Enumerate() em Python é uma função que permite iterar sobre uma estrutura de dados(como uma lista, tupla ou outro objeto iterável).
# A função Enumerate() retorna um objeto Enumerate, que pode ser  usado em loops para percorrera estrutura de dados e acessar o contador e o valorde cada elemento.

seq = {'a','b','c'}

a = list(enumerate(seq))

print(a)

for indice, valor in enumerate(seq):
    print(indice,valor)


for indice, valor in enumerate(seq):
    if indice >= 2:
        break
    else:
        print (valor)    


lista = ['Marketing','Tecnologia', 'Business']

for i, item in enumerate(lista):
    print(i,item)

for i, item in enumerate('Data Scinence Academy'):
    print(i,item)

for i, item in enumerate(range(10)):
    print(i,item)
