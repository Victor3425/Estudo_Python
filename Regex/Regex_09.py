import re

#Médotos para checagem:


texto = 'arara'
p1 = re.compile(r'a')
check_findall = p1.findall(texto)
check_match = p1.match(texto)
print(check_findall)
print(check_match)
print(texto[0:2])