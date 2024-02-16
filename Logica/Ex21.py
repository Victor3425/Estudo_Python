numeros = [int(x) for x  in input('Digite os números separados por espaço: ').split()]

n = len(numeros)
for i in range(n -1):
    for j in range(0, n - i - 1):
        if numeros[j]> numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros[j + 1], numeros[j]

print(numeros)

b = len(numeros)
for i in range(n -1):
    for j in range(0, n - i - 1):
        if numeros[j] < numeros[j + 1]:
            numeros[j], numeros[j + 1] = numeros [j + 1], numeros[j]            

print(numeros)            
