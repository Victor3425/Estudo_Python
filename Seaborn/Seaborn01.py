import random
import numpy as np 
import pandas as pd 
import matplotlib as mt 
import matplotlib.pyplot as plt 
import warnings
warnings.filterwarnings('ignore')
import seaborn as sea 

# Carregando um dos datasets que vem com o Seaborn
dados = sea.load_dataset('tips')
dados.head()
print(dados)

# O método joinplot cria plot de 2 variáveis com gráficos bivariados e univariados
sea.jointplot(data= dados, x = 'total_bill', y= 'tip', kind= 'reg')

# O método implot() cria plot com dados e modelos de regressão
sea.lmplot(data= dados, x= 'total_bill', y= 'tip',col='smoker')

# Construindo um dataframe com Pandas
df = pd.DataFrame()

# Alimentando o Dataframe com valores aleatórios
df['Idade']= random.sample(range(20,100),30)
df['Peso']= random.sample(range(55,150),30)

df.shape
df.head()

# Implot
sea.lmplot(data = df, x= 'Idade',y='Peso',fit_reg = True)

# kdeplot
sea.kdeplot(df.Idade)

# kdeplot
sea.kdeplot(df.Peso)

# distplot
sea.displot(df.Peso)

# Histograma
plt.hist(df.Idade, alpha= .3)
sea.rugplot(df.Idade)

# Box Plot
sea.boxenplot(df.Idade,color='m')

# Box Plot
sea.boxenplot(df.Peso, color='y')

# Violin Plot
sea.violinplot(df.Idade,color='g')

# Violin Plot
sea.violinplot(df.Peso, color='cyan')

# Clustermap
sea.clustermap(df)

plt.show()