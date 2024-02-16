import re

texto = 'arara'

# ^ = Irá testar o inicio da string
# [^] = Irá considerar todos os caracteres EXETO o indicado

p1 = re.compile(r'^a')
p2 = re.compile(r'[^a]')

check1 = p1.findall(texto)
check2 = p2.findall(texto)

print(check1)
print(check2)
