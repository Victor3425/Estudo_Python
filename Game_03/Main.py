from Introducao import introducao, menu_inicio
from Parte_01 import Morcegos, opcao1, Morreu_Morcegos,Print_Labirinto


def main():
    introducao()
    comecar = menu_inicio()


    if comecar == 1:
            Morcegos()
            opc1 = opcao1()
            
            if opc1 == 1:
                 Morreu_Morcegos()

            else:
                 Print_Labirinto()     

    else:
        print('Opção inválida')



    
if __name__ == "__main__":
    main()