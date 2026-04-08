#importando as bibliotecas necessárias
import numpy as np
import matplotlib.pyplot as plt 

# dados de x e y para o gráfico
x = [1,2,3,4,5]
y = [2,5,7,8,11]
# função do grafico
def plot_graph(x, y,):
    #variáveis para o título e os rótulos dos eixos
    title = "Gráfico de Dispersão"
    xlabel = "Eixo X"
    ylabel = "Eixo Y"
    # função da reta
    z = np.polyfit(x,y,1)

    a = z[0]
    b = z[1]

    #grafico de dispersão
    plt.scatter(x, y, label ="Dados Experimentais")

    #função da reta
    p = np.poly1d(z)

    #equação 
    equacao = (f"y = {a:.2f} x +{b:.2f}")

    #linha de tendência
    plt.plot(x, p(x), "r--", label = "Linha de Tendência")

    #configurações do gráfico
    plt.title(title)
    plt.text(1,9,equacao, fontsize=12, bbox=dict(facecolor='white'))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid(True)
    plt.show()

# chamada da função do grafico
plot_graph(x, y)
