import re

class teste():

    def textoxml(self,texto):
        self.texto = texto
    

pdtx = teste(texto = """16.765.826/0023-85""")

pd = re.findall(r'[0-9]{2}.[0-9]{3}.[0-9]{3}/[0-9]{4}-[0-9]{2}',pdtx)

pd1 = "".join(pd)

print(pd1)