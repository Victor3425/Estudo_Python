# Criando a classe animal - Super-classe
# Classe mãe

class Animal:

    def __init__(self):
        print('Animal criado')

    def imprimir(self):
        print('Esse é um animal')    

    def comer(self):
        print('Hora de comer')

    def emitir_som(self):
             pass   
    
# Criando a classe cachorro - sub-classe    

class Cachorro(Animal):
     
     def __init__(self):
          Animal.__init__(self)
          print('Objeto Cachorro criado')

     def emitir_som(self):
          print('Au au!')     

# Criando a classe cachorro - sub-classe    

class Gato(Animal):
     
     def __init__(self):
          Animal.__init__(self)
          print('Objeto Gato criado')

     def emitir_som(self):
          print('Miau!')            

rex = Cachorro()
rex.emitir_som()
rex.imprimir()
rex.comer()
zeze = Gato()
zeze.emitir_som()
zeze.imprimir()
zeze.comer()



