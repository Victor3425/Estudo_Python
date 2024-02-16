import matplotlib.pyplot as plt
from pylab import *

# Dados 
x = linspace(0,5,10)
y = x ** 2

# Criar os subplots
fig, axes = plt.subplots(1,2, figsize=(10,4))

# Criar o plot1
axes[0].plot(x,x**2, x, exp(x))
axes[0].set_title('Escala Padrão')

# Criar o plot2
axes[1].plot(x, x**2,x,exp(x))
axes[1].set_yscale('log')
axes[1].set_title('Escala Logaritmica (y)')

plt.show()
