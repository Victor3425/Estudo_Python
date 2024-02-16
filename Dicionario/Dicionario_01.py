
#Isso é uma lista
estudante_lst = ["Pedro", 24, "Ana", 22, "Ronaldo", 26, "Janaina",25]

#print(estudante_lst)

#print(type(estudante_lst))

#Isso é um dicionário
estudante_dic = {"Pedro": 24, "Ana": 22, "Ronaldo": 26, "Janaina": 25}

#print(estudante_dic)

#print(type(estudante_dic))

#print(estudante_dic["Pedro"])

estudante_dic["Marcelo"] = 23

#print(estudante_dic["Marcelo"])

#Apagar as informaçoes de dentro do dicionario
#estudante_dic.clear()

#print(estudante_dic)

#Apagar o dicionario da memoria
#del estudante_dic

#print(estudante_dic)

#Mostrar as chaves
#print(estudante_dic.keys())

#Mostrar o tamanho 
#print(len(estudante_dic))

#Mostra os valores
#print(estudante_dic.values())

#Mostra todos os items 
#print(estudante_dic.items())

estudantes2 = {"Camila":27, "Adriana":28, "Roberta":26}

#Juntar o dicionario "estudantes2" com o dicionario "estudantes_dic"
estudante_dic.update(estudantes2)

print(estudante_dic)
