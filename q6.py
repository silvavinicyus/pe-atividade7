import matplotlib.pyplot as plt
import numpy as np
import random

def quest6():  
  #Abertura do arquivo com os dados da questão
  arq = open('dados/chromosome_position_data.txt', 'r')

  #Arrays para guardar os valores de Mut1, Mut2 e WT
  mut1 = []
  mut2 = []  
  wt = []

  #Repetição que percorre o arquivo com os dados da questão, selecionando e adicionando os valores de idade e peso aos seus respectivos arrays
  for linha in arq:    
    linha = linha.split('\t')
    
    if('Position' not in linha):      
      mut1.append(float(linha[1]))
      mut2.append(float(linha[2]))
      wt.append(float(linha[3][:-1]))
  
  # Utilização do matplotlib para plotagem do gráfico
  plt.plot(mut1, color='red')
  plt.plot(mut2, color='blue')
  plt.plot(wt, color='green')

  #Definição dos labels dos eixos x e y
  plt.ylabel("Valor")
  plt.xlabel("Posição com o cromossomo")

  # Função que permiti criar ume legenda para definir o que cada linha significa
  plt.legend(['Mut1', 'Mut2', 'WT'], bbox_to_anchor=(0.2, 1), loc="upper right")
  
  #Função que plota o gráfico na tela
  plt.show()

quest6()