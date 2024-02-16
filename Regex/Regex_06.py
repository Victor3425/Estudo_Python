import re 

texto = 'arara1992'

# \d = Qualquer caracter que SEJA um algarismo de 0 a 9
# \D = Qualquer caracter que NÃO SEJA um algarismo de 0 a 9
p1 = re.compile(r'\d')
p2 = re.compile(r'\D')

check1 = p1.findall(texto)
check2 = p2.findall(texto)

print(check1)
print(check2)

