def askinit():
    try:
        val = int((input('Digite um número: ')))
    except:
        print('Você não digitou um número! ')
        val = int((input('Tente novamente. Digite um número: ')))
    finally:
        print('Obrigado!')    

askinit()


def askinit():
    while True:
        try: 
            val = int(input('Digite um número: '))
        except:
            print('Você não digitou um número!')
            continue
        else:
            print('Obrigado por digitar um número!') 
            break
        finally:
            print('Fim da execução!')
        print(val)    

askinit()              