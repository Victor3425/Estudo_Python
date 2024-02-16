# Criando Gráfico Customizados com Pylab
# Pylab é um módulo fornecido pela biblioteca Matplotlib que combina a funcionalidade do pacote NumPy com a funcionalidade do pacote pyplot.

import matplotlib.pyplot as plt
from pylab import *

# Gráfico de linha

# Gráfico com linha é um tipo de plotagem usado para representar a evolução do comportamento de uma variável com diferentes pontos de dados.
# OS gráficos de linha são úteis para visualizar tendências e padrões em dados.

x = linspace(0,5,10)
y = x ** 2

fig = plt.figure()

axes = fig.add_axes([0,0,0.8,0.8])

axes.plot(x,y, 'r')

axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_title('Gráfico de Linha')

plt.show()
