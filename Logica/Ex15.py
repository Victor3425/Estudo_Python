import math

A = float(input())
B = float(input())
C = float(input())

resultado_A = (A*C)/2
resultado_B = math.pi*(C**2)
resultado_C = ((A+B)*C)/2
resultado_D = B **2
resultado_E = A * B


print('TRIANGULO: {:.3f}'.format(resultado_A))
print('CIRCULO: {:.3f}'.format(resultado_B))
print('TRAOEZIO: {:.3f}'.format(resultado_C))
print('QUADRADO: {:.3f}'.format(resultado_D))
print('RETANGULO: {:.3f}'.format(resultado_E))
