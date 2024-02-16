import pandas as pd
from pandas import DataFrame
import numpy as np

df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Pandas\dataset.csv',sep=',')

# Filtramos o dataframe pela coluna Segmento com valores que inicia com letras 'Con'
a = df[df.Segmento.str.startswith('Con')].head()

print(a)

