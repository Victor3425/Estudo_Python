import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 2344012"

# qual o padrão do CEP?

# 5 dígitos + hifen(opcional) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")

# ou

padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")

# ou

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")


#Dicionário da função

### re.compile("

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[-]? - procurar um hifen... dentro do padrão... caso eu coloque um interrogação ? após o colchets, pode ser que não necessariamente terá um hifen nessa posição.

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###[0123456789] - números que contem no CEP... na mesma quantidade de vezes em que se exibe

###")


###re.compile("

###[0123456789]

###{5} - quantidade de vezes que a sequência anterior de caracteres aparece

###[-]?

###[0123456789]

###{3} - quantidade de vezes que a sequência anterior de caracteres aparece

###")

busca = padrao.search(endereco)

if busca:

 cep = busca.group()

 print(cep)

else :
 print('CEP não encontrado')

#Ora para extrair o valor que esteja de acordo com o padrão fornecido (search), ora para verificar se o texto está de acordo com o padrão (match).