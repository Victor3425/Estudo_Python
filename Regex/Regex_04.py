import re


texto = "arara arabra arabla"

# . = Entender qualquer valor exceto uma nova linha
# \. = Para buscar o caracter
padrao = re.compile(r'ar.bla')

check = padrao.findall(texto)

print(check)
