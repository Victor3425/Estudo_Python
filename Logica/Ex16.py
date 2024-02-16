A = int(input())
B = int(input())
C = int(input())

resultado = (A+B+abs(A-B))/2
resultado = (resultado + C + abs(resultado - C))/2

total_resultado = int(resultado)

print(total_resultado,'eh o maior')