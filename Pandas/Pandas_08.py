import pandas as pd
from pandas import DataFrame
import numpy as np

df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Pandas\dataset.csv',sep=',')


a = df['ID_Pedido']

b = df['ID_Pedido'].str.split('-').head()

c = df['ID_Pedido'].str.split('-').str[1].head()

d = df['Data_Pedido'].head(3)

e = df['Data_Pedido'].str.lstrip('20').head()

print(e)