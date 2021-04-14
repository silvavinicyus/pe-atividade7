import matplotlib.pyplot as plt
import numpy as np
import random

def quest7():
  #Abertura do arquivo com os dados da questão
  arq = open('dados/brain_bodyweight.txt', 'r')
  
  for linha in arq:
    linha = linha.split('\t')

    #Repetição que percorre o arquivo com os dados da questão, plotando os pontos em suas coordenadas e adicionando sua margem de erro
    if ('Bodyweight ' not in linha):      
      yposition = float(linha[1])
      xposition = float(linha[2])

      xerror = float(linha[4])
      yerror = float(linha[3])

      text = str(linha[0])      

      #Função que plota um ponto e adiciona sua margem de erro para + e -
      plt.errorbar(xposition, yposition, yerr=yerror, xerr=xerror, color='black', marker='d', capsize=4)
      #Função que adiciona uma pequena legenda para cada ponto
      plt.text((xposition-0.15), (yposition-0.3), s=text,fontdict=dict(size=6))  
  
  # Definindo os valores para os labels de x e y
  plt.xlabel('Peso do cérebro')
  plt.ylabel('Peso do corpo')

  # Definindo os valores para os rótulos dos eixos x e y
  plt.yticks([-1, 0, 1, 2, 3, 4, 5])
  plt.xticks([0, 1, 2, 3])
  
  #Função que plota o gráfico na tela
  plt.show()
  
quest7()