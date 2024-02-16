nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

pesoNota1 = 2
pesoNota2 = 3
pesoNota3 = 4
pesoNota4 = 1

media = (nota1 * pesoNota1+ nota2*pesoNota2 + nota3 * pesoNota3 + nota4 * pesoNota4) / (pesoNota1 + pesoNota2 + pesoNota3 + pesoNota4)


if media >= 7.0:
    print(media)
    print('Aluno Aprovado') 

elif media < 5.0:
    print(media)
    print('Aluno Reprovado')

elif media >= 5.0:
    print(media)
    print('Aluno em exame')
    exame = float(input('Digite a nota do exame:'))
    mediaExame = (exame + media) /2
    if mediaExame >= 7.0:
        print('Aluno aprovado')
        print('Media final: ' + mediaExame)
    else:
        print(mediaExame)
        print('Reprovado')


elif media <= 6.9:
    print(media)
    print('Aluno em exame.')           
    exame = float(input('Digite a nota do exame:'))
    mediaExame = (exame + media) /2
    if mediaExame >= 7.0:
        print('Aluno aprovado')
        print('Media final: ' + mediaExame)
    else:
        print(mediaExame)
        print('Reprovado')

