# Gráfico de Pizza
# Gráfico de Pizza(Pie Plot), também conhecido como gráfico de setores, é um tipo de plotagem que representa a compocição de uma variaável
# categórica em relação ao todo. Ele é representado por um círculo dividido em fatias que representam as proporções relativas das categorias.

import matplotlib.pyplot as plt

fatias = [7,2,2,13]
atividades = ['dormir', 'comer', 'passear', 'trabalhar']
cores = ['olive', 'lime','violet','royalblue']

plt.pie(fatias, labels= atividades, colors= cores, startangle= 90, shadow= True, explode= (0,0.2,0,0))
plt.show()