from pandas import DataFrame
import numpy as np


dados = {'Estado': ['Santa Catarina','Rio de Janeiro','Tocantis','Bahia','Minas Gerais'],'Ano': [2004,2005,2006,2007,2008],'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}
DataFrame(dados, columns= ['Estado','Taxa Desemprego','Ano'])

df2 = DataFrame(dados,
                columns= ['Estado', 'Taxa Desemprego', 'Taxa Crecimento', 'Ano'],
                index= ['estado1','estado2','estado3','estado4','estado5'])


# Resumo estatístico do Dataframe
#print(df2.describe())

# Usando o NumPy para alimentar uma das colunas do dataframe
df2['Taxa Crecimento'] = np.arange(5.)

#print(df2)

# Resumo estatístico do Dataframe
print(df2.describe())