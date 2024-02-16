preco = 500

def calcular_imposto(preco):
    return preco * 0.3 

print(calcular_imposto(preco))



calcular_imposto2 = lambda x: x * 0.3

print(calcular_imposto2(preco))


precos = [100,500,10,25]

imposto = list(map(lambda x:x*0.3,precos))
print(imposto)