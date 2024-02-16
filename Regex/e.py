import re

texto = "Texto que contém a palavra CLARO S.A. em algum lugar."

padrao = re.compile(r'\bCLARO S\.A\.\b', texto)
resultado = padrao.search(texto)

if resultado:
    print(resultado.group())
