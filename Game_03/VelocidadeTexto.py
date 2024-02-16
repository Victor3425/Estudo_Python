import time


def print_devagar01(texto1):
    for caractere in texto1:
        print(caractere, end='', flush=True)
        time.sleep(0.1)


def print_devagar02(texto2):
    for caractere in texto2:
        print(caractere, end='', flush=True)
        time.sleep(0.2)