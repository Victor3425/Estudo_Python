A = int(input('Escolha a conversão (1 para Celsius -> Fahrenheit, 2 para Fahrenheit -> Celsius): '))

if A == 1:
    celsius = float(input('Digite a temperatura em graus Celsius: '))
    conversao_celsius = (celsius * 9/5) + 32
    print(f'{celsius} graus Celsius é igual a {conversao_celsius:.2f} Fahrenheit.')
elif A == 2:
    fahrenheit = float(input('Digite a temperatura em graus Fahrenheit: '))
    conversao_fahrenheit = (fahrenheit - 32) * 5/9
    print(f'{fahrenheit} graus Fahrenheit é igual a {conversao_fahrenheit:.2f} Celsius.')
else:
        print('Opção inválida. Escolha 1 ou 2 para a converção.')