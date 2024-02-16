def calcular_media_ponderada(notas, pesos):
    return sum(nota * peso for nota, peso in zip(notas, pesos)) / sum(pesos)

notas = [float(input(f'Digite a nota {i + 1}: ')) for i in range(4)]
pesos = [2,3,4,1]

media = calcular_media_ponderada(notas, pesos)

print(f'Média: {media:.2f}')

if media >= 7.0:
    print('Aluno Aprovado')
elif media < 5.0:
    print('Aluno Reprovado')
else:
    print('Aluno em exame')
    exame = float(input('Digite a nota do exame: '))
    media_exame = calcular_media_ponderada([media, exame], [1,1])        

    if media_exame >= 7.0: 
        print('Aluno Aprovado')
    else: 
        print('Reprovado')    

    print(f'Média final: {media_exame:.2f}')    