
#A condição tem que deixar de ser verdadeira pelo menos uma vez, senão pode travar o computador
valor=0
while valor <10:
    print(valor)
    valor=valor+1


#Para entrar no loop while a condição tem que ser verdadeira
    valor = 11
    while valor <10:
        print(valor)
        valor = valor+1

#Também é possível usar a claúsula else para encerrar o loop while
x = 0 

while x<10:
    print('O valor de x nesta iteração é:', x)
    print('x ainda é menor que 10, somando 1 a x')
    x+=1

else:
    print('Loop concluído!')
print(x)       


# Se encontramos o número 4 interrompemos o loop
valor = 0
while valor<10:
 if valor == 4:
    break
 else:
    pass
 print(valor)
 valor = valor +1 

 #Desconsideramos a letra z ao imprimir os caraxteres da frase
 for letra in 'Python é zzzzz incrível!':
    if letra == 'z':
       continue
    print(letra)
