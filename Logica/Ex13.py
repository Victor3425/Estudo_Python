
resultado = 0

for i in range(2):
    cod_peca = int(input())
    num_peca = int(input())
    valor_peca = float(input())
    resultado += valor_peca  * num_peca
  

print('VALOR A PAGAR: R$ {:.2f}'.format(resultado))