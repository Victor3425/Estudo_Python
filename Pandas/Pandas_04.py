import pandas as pd
from pandas import DataFrame
import numpy as np

dsa_df = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Pandas\dataset.csv',sep=',')

#print(dsa_df)

# head é um limitador
#print(dsa_df.head(2))

print(dsa_df.isna().sum())


# A moda em Estatística é uma medida de tendência central que representa o valor mais frequente em um conjunto de dados.

# A moda é espeecialmente útil quando queremos saber qual é o valor mais comum ou popular em um conjunto de dados, seja em uma distribuição unimodal
#(com apenas uma moda) ou em uma distribuição bimodal(com duas modas).

# No entanto, a moda pode não ser tão representativa quanto outras medidas de tendência central, como a média e a mediana, especialmente em distribuições 
# assimétricas ou quando há valores extros. Por essa razão, é importante analisar diferentes medidas de tendência central e usar a que melhor se 
# adequa aos objetivos de análise estatística.



# Extraímos a moda da coluna Quantity
moda = dsa_df['Quantidade'].value_counts().index[0]
#print(moda)

