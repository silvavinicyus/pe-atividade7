import matplotlib.pyplot as plt
import numpy as np
import random

def quest4():
  #Abertura do arquivo com os dados da questão
  arq = open('dados/male_female_counts.txt', 'r')

  #Arrays para guardar os valores de sample e count
  sample = []
  count = []

  #Repetição que percorre o arquivo com os dados da questão, selecionando e adicionando os valores de idade e peso aos seus respectivos arrays
  for linha in arq:    
    linha = linha.split('\t')
    
    if('Sample' not in linha):
      sample.append(linha[0])
      count.append(int(linha[1][:-1])) 
  
  # Função do matplotlib que define o tamanho da figura a ser plotada  
  fig, ax1 = plt.subplots(figsize=(7,4))

  # Função do matplotlib que plota um gráfico de barras na vertical
  ax1.bar(sample, count, edgecolor='k', color=['red', 'orange', 'yellow', 'green', 'lime', 'turquoise', 'blue', 'darkblue', 'purple', 'pink'], width=0.8)
  
  #Função para tirar as bordas do gráfico
  plt.box(False)  

  #Função que faz o gráfico não cortar os títulos do eixo y
  plt.tight_layout()
  
  # Definição do tamanho da fonte dos rótulos do eixo x
  plt.xticks(fontsize=8)

  #Definição dos valores do eixo y
  plt.yticks([0, 5, 10, 15])

  #Função que plota o gráfico na tela
  plt.show()

quest4()