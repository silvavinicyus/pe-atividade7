import matplotlib.pyplot as plt
import numpy as np
import random

def quest2():
  #Abertura do arquivo com os dados da questão
  arq = open('dados/feature_counts.txt', 'r')

  #Arrays para guardar os valores de feature e count
  feature = []
  count = []

  #Repetição que percorre o arquivo com os dados da questão, selecionando e adicionando os valores de idade e peso aos seus respectivos arrays
  for linha in arq:     
    linha = linha.split('\t')
    
    if('Feature' not in linha):
      feature.append(linha[0])
      count.append(int(linha[1][:-1])) 
  
  # Função do matplotlib que define o tamanho da figura a ser plotada
  fig, ax1 = plt.subplots(figsize=(6,5))

  # Função do matplotlib que plota um gráfico de barras na horizontal
  ax1.barh(feature, count, edgecolor='k', facecolor='gray')
  #Função para tirar as bordas do gráfico
  plt.box(False)  
  #Definição dos valores do eixo x
  plt.xticks([0, 20000, 40000, 60000])
  #Definição do label do eixo x
  plt.xlabel('Numero de aparecimentos')
  #Função que faz o gráfico não cortar os títulos do eixo y
  plt.tight_layout()
  #Função que plota o gráfico na tela
  plt.show()

quest2()