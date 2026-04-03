#importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt 

# dados de x e y para o gráfico
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# gráfico de dispersão
plt.scatter(x, y) #e possivel melhorar a logica do grafico
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid()
plt.show()