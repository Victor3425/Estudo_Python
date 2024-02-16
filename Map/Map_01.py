# A função map() em Python é a função que aplica uma determinada função a cada elemento de uma estrutura de dados iterável(como uma lista, tupla ou outro objeto iterável). 
# A função map() retorna um objeto que pode ser convertido em outra estrutura de dados, como uma lista, se necessário

# Função em Python que retorna um número ao quadrado
def potencia(x):
    return x ** 2

numeros = [1,2,3,4,5]

numeros_ao_quadrado = list(map(potencia, numeros))

print(numeros_ao_quadrado)


# Função 1 -  Recebe uma temperatura como parâmetro e retorna a temperatura em Fahrenheit
def fahrenheit(T):
    return ((float(9)/5)*T + 32)

def celsius(T):
    return (float(5)/9)*(T-32)

temperaturas = [0,22.5,40,100]

# Em Python 3, a função map() retorna um iterator 
map(fahrenheit, temperaturas)

a = list(map(fahrenheit, temperaturas))

print(a)



