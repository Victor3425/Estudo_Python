def verificarPar(num):
    if num % 2 ==0:
        return True
    else:
        return False
    
verificarPar(36)

lista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]

a = list(filter(verificarPar, lista))

b = list(filter(lambda x: x%2 == 0 , lista))

c = list(filter(lambda num: num > 8, lista))

print(a)
print(b)
print(c)