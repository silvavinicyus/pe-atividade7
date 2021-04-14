import matplotlib.pyplot as plt
import numpy as np
import random

def quest5():
  #Abertura do arquivo com os dados da questão
  arq = open("dados/up_down_expression.txt", 'r')

  #Arrays para guardar os valores de up, down e unchanging
  upx = []
  upy = []

  downx = []
  downy = []

  unchangingx = []
  unchangingy = []

  #Repetição que percorre o arquivo com os dados da questão, selecionando e adicionando os valores de idade e peso aos seus respectivos arrays
  for linha in arq:    
    linha = linha.split('\t')
    
    if('Gene' not in linha):      
      if(linha[3][:-1] == 'up'):
        upx.append(float(linha[1]))
        upy.append(float(linha[2]))        
      elif(linha[3][:-1] == 'down'):
        downx.append(float(linha[1]))
        downy.append(float(linha[2]))
      elif(linha[3][:-1] == 'unchanging'):
        unchangingx.append(float(linha[1]))
        unchangingy.append(float(linha[2]))
  
  # Função que plota um gráfico de dispersão
  plt.scatter(upx, upy, color='red', marker='o')
  plt.scatter(unchangingx, unchangingy, color='gray', marker='o')
  plt.scatter(downx, downy, color='blue', marker='o')

  #Definição dos labels dos eixos x e y
  plt.xlabel("Condição 1")
  plt.ylabel("Condição 2")

  #Definição dos valores do eixo y
  plt.yticks([0, 5, 10])

  #Definição dos valores do eixo x
  plt.xticks([0, 5, 10])

  #Função que plota o gráfico na tela
  plt.show()

quest5()