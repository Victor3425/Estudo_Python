from pandas import DataFrame

dados = {'Estado': ['Santa Catarina','Rio de Janeiro','Tocantis','Bahia','Minas Gerais'],'Ano': [2004,2005,2006,2007,2008],'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}

# Converte o dicionario em um Dataframe
df = DataFrame(dados)

# Visualiza as 5 primeiras linhas
#print(df.head())

#print(type(df))

# Reorganizando as colunas
DataFrame(dados, columns= ['Estado','Taxa Desemprego','Ano'])

df2 = DataFrame(dados,
                columns= ['Estado', 'Taxa Desemprego', 'Taxa Crecimento', 'Ano'],
                index= ['estado1','estado2','estado3','estado4','estado5'])

#print(df2.values)
#print(df2.dtypes)
print(df2.columns)