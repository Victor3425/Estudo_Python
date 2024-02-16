from pandas import DataFrame
import numpy as np


dados = {'Estado': ['Santa Catarina','Rio de Janeiro','Tocantis','Bahia','Minas Gerais'],'Ano': [2004,2005,2006,2007,2008],'Taxa Desemprego':[1.5,1.7,1.6,2.4,2.7]}
DataFrame(dados, columns= ['Estado','Taxa Desemprego','Ano'])

df2 = DataFrame(dados,
                columns= ['Estado', 'Taxa Desemprego', 'Taxa Crecimento', 'Ano'],
                index= ['estado1','estado2','estado3','estado4','estado5'])

#print(df2['estado2':'estado4'])

print(df2[ df2['Taxa Desemprego']<2])