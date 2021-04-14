import matplotlib.pyplot as plt
import numpy as np
import random

def quest3():
  # Definição dos valores da ditribuição normal padrão com 10 mil elementos
  values = np.random.normal(loc=0,scale=1,size=10000)
  values2 = np.random.normal(loc=4,scale=1,size=10000)

  # Concatenando os 2 valores para que seja possível plotar o gráfico de ambos
  valuesfinal = np.concatenate((values, values2))

  #Plote do histograma com os dados gerados anteriormente
  plt.hist(valuesfinal, color='k', bins=110, edgecolor='k' , facecolor='white')  
  
  #Função para tirar as bordas do gráfico
  plt.box(False)
  
  #Definição do título do gráfico
  plt.title('Histograma de duas Distribuições Normais Padrão')
  
  #Definição dos labels dos eixos x e y
  plt.xlabel("Valores")
  plt.ylabel('Frequência')
  
  #Função que plota o gráfico na tela
  plt.show()

quest3()