import re

#\s = Qualquer caracter qu e SEJA vazio
# \S = Qualquer caracterque NÃO SEJA vazio

texto = '''arara 1992''' ' '


p1 = re.compile(r'\s')
p2 = re.compile(r'\S')

check1 = p1.findall(texto)
check2 = p2.findall(texto)

print(check1)
print(check2)