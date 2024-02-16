import re 

#\w = Qualquer caracter que SEJA alfanumerico
#\W = Qualquer caracter que NÃO SEJA alfanumerico

texto = 'arara@ 1992_'

p1 = re.compile(r'\w')
p2 = re.compile(r'\W')

check1 = p1.findall(texto)
check2 = p2.findall(texto)

print(check1)
print(check2)