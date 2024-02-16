vendedor = 'Victor'

vendas = 1000
meta = 500

if vendas >= meta:
    print('Você bateu a meta')
else:
    print('Não bateu a meta')    


class Vendedor():
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

        