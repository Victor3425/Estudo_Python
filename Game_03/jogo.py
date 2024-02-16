import time 

def print_devagar01(texto1):
    for caractere in texto1:
        print(caractere, end='', flush=True)
        time.sleep(0.1)


def print_devagar02(texto2):
    for caractere in texto2:
        print(caractere, end='', flush=True)
        time.sleep(0.2)

print_devagar01('-----------------------\n')
print_devagar02('Caverna misteriosa\n')
print_devagar01('-----------------------\n')
comecar = int(input('Aperte 1 para começar: '))

if comecar == 1:
    
    while True:
        print_devagar01('-----------------------\n')
        print_devagar02('Tente sair da caverna\n')
        print_devagar01('-----------------------\n')

        print_devagar02("Você é atacado por morcegos, o que você faz?\n")
        print_devagar01('-----------------------\n')
        print_devagar02('1- Sai correndo\n')
        print_devagar02('2- Pega uma tocha na parede para se defender\n')
        morcegos = int(input())
        break
