import re

text = "Toyota Supra"

#search significa pesquisar, mais diferente do findall ele nao retorna uma coleçao
#E com ele eu consigo usar os metodas start e end
res = re.search(r'S',text)

#Start é para saber a posicao. print(res.start())
#End é para saber a posicao final.print(res.end())

if (res != None):
    pi = res.start()
    pf = res.end()
    tam = pf - pi

    print(res.start())
    print(res.end())
    print(tam)

else:
    print("Não encontardo")