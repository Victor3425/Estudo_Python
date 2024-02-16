import re

texto = 'CNPJ 15.132.325/25.1535'

a = re.findall(r'CNPJ (\w+)',texto)

print(a)

texto2 = '84680000001-6 24440162202-6 31120038000-5 00346303525-7'

b = re.findall(r'\d{11}-{1}\d',texto2)
b = ''.join(b)
#print(b)

texto3 = 'NET SERVICOS 0040128223707'

c = re.findall(r'NET SERVICOS \d+',texto3)

#print(c)

texto4 = 'Outubro/2023'

d = re.findall(r'\b(?:Janeiro|Fevereiro|Março|Abril|Maio|Junho|Julho|Agosto|Setembro|Outubro|Novembro|Dezembro)\/\d{4}\b',texto4)

#print(d)


texto5 = 'Texto que contém a palavra CLARO S.A. em algum lugar.'

e = re.findall(r'[C][L][A][R][O][ ][S][.][A][.]',texto5)

#print(e)


texto6 = '09550-050   SAO CAETANO DO SUL  SP'

f = re.findall(r'^(.*?)(?<!\d[\d\s\-])\s*(\S+)$',texto6)

#print(f)

texto7 = '84610000000-5 16650162202-0 31115143000-7 00280282485-0'

g = re.findall(r'\b\d+-\d\b',texto7)

g = ''.join(g)

#print(g)

texto8 = '052/010849691'

h = re.findall(r'[0-9]{3}/[0-9]{9}',texto8)

#print(h)


texto9 = '53519,03'

j = re.findall(r'\d+,\d+',texto9)

#print(j)

texto10 = '00.944.145/0015-46'

k = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}',texto10)

#print(k)


texto11 = '04028-002   SAO PAULO  SP'

j = re.findall(r'(\d{5}-\d{3})\s+([A-Z\s]+)\s+([A-Z]{2})',texto11)

#print(j)


texto = '04028-002 SAO PAULO SP'


#padrao = re.findall(r'(\d{5}-\d{3})', texto)
#padrao2 = re.compile(r'(\b[A-Za-z]+\b)',texto)

#correspondencia = padrao2.search(texto)

#cidade = ''.join(correspondencia)
#correspondencia = str(correspondencia)

#cidade = correspondencia.group(2).strip()
#cep = padrao
#cidade = padrao2
#endereco3 = ''.join(texto)
#cep = ''.join(cep)
#cidade = ''.join(map(str,cidade))


#print(cep)
#print(cidade)

