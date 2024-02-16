import pandas as pd
from pandas import DataFrame
import numpy as np

df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Pandas\dataset.csv',sep=',')


# groupby() junta as colunas e o mean() calcula a media 
a = df [['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).mean()
b = df[['Segmento','Regiao','Valor_Venda']].groupby(['Segmento','Regiao']).agg(['mean','std','count'])

print(b)