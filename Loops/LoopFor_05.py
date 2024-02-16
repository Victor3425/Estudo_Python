#Loop em lista de lista (matrizes) para encontrar o maior número

matriz = [[42,23,34], [100,215,114], [10.1,98.7,12.3]]
maior_numero = 0

#Loop externo 
for linha in matriz:

    #Loop interno
    for num in linha:

        #Condicional
        if num > maior_numero:
            maior_numero=num

print('Maior número:', maior_numero)        

#Listando as chaves de um dicionário
dict = {'k1': 'Python','k2':'R','k3':'Scala'}
for item in dict:
    print(item)

#Imprimindo chave e valor do dicionário. Usando o método items() para retornar os items de um dicionário
for k,v in dict.items():
    print(k,v)    

