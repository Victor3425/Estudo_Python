import re

texto = "Teste"
tex = "supra"

pesquisa = input(r'Pesquisar: ')
#findall significa encontrar
res = re.findall(pesquisa,texto)
rest = re.findall(pesquisa,tex)
#res = re.findall("s", texto)
#rest = re.findall("pra", tex)

print(res)
print(rest)

for t in rest:
    print(t)
    for a in res:
        print(a)



