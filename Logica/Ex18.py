print('Codigo     Especificacao     Preço \n1         Cachorro Quente    R$4.00\n2         X-Salada           R$4.50\n3         X-Bacon            R$5.00\n4         Torrada simples    R$2.00\n5         Refrigerante       R$1.50    ')

total = 0
 
while True:
    codigo = int(input('Digite o código do produto (ou 0 para encerrar): '))


    if codigo == 0:
        break
    
    quantidade = int(input('Digite a quantidade desejada: '))

    if codigo == 1:
        total += 4.00 * quantidade
    elif codigo == 2:
        total += 4.50 * quantidade
    elif codigo ==3:
        total += 5.00 * quantidade
    elif codigo ==4:
        total += 2.00 * quantidade
    elif codigo ==5:
        total += 1.50 * quantidade
    else:
        print('Código inválido. Tente novamente.')


print(f"Total: R${total:.2f}")            
