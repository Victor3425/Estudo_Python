import re

texto = """Ainda bem que você abriu esse tópico, há um erro nessa Paula6534_345@caoa.com.br regex, o ponto (.) não está Vitaoregex24@gmail.com sendo visto como "ponto" e sim victor.rodrigues@hotmal.com como um meta-carácter da própria regex que significa qualquer coisa."""

 

pd = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b" ,texto)

pd1 = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
 

for pd in pd: 

    def isValid(email):
        if re.fullmatch(pd1,email):
            print("Email válido")
        else:
            print("Email inválido")

    print(pd)

isValid(pd)
