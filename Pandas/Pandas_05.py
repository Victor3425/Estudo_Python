import pandas as pd
from pandas import DataFrame
import numpy as np

df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Pandas\dataset.csv',sep=',')

# head tras os primeiros registros
a = df[ (df.Segmento == 'Home Office') & (df.Regiao == 'South') ].head()

# taiil tras os ultimos registros
c = df[ (df.Segmento == 'Home Office')| (df.Regiao == 'South')].tail()

# sample tras os registros de forma aleatoria
b = df[ (df.Segmento != 'Home Office') & (df.Regiao != 'South')].sample(5)


print(c)