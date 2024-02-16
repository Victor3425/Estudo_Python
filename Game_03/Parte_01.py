from VelocidadeTexto import print_devagar01, print_devagar02


def Morcegos():
        print_devagar01('-----------------------\n')
        print_devagar02('Tente sair da caverna\n')
        print_devagar01('-----------------------\n')

        print_devagar02("Você é atacado por morcegos, o que você faz?\n")
        print_devagar01('-----------------------\n')
        print_devagar02('1- Sai correndo\n')
        print_devagar02('2- Pega uma tocha na parede para se defender\n')
        
def opcao1():
  return int(input())    


def Morreu_Morcegos():
   print_devagar01('Você morreu') 

def Print_Labirinto():
        print_devagar01('Você acaba entarndo em um labirinto\n')
        print('''###################################
###################################
###################################
#################### '--' '--' '--'
#################### '--' #### '--'
#'--' '--' '--' #### '--' #### '--'
#'--' #### '--' #### '--' #### '--'
#'--' #### '--' '--' '--' #### '--' '--''')

