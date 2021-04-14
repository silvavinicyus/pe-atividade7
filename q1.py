import matplotlib.pyplot as plt
import numpy as np
import random

def quest1():
  #Abertura do arquivo com os dados da questão
  arq = open('dados/weight_chart.txt', 'r')

  #Arrays para guardar os valores de idade(age) e peso (weight)
  age = []
  weight = []  

  #Repetição que percorre o arquivo com os dados da questão, selecionando e adicionando os valores de idade e peso aos seus respectivos arrays
  for linha in arq:    
    linha = linha.split('\t')
    
    if('Age' not in linha):
      age.append(int(linha[0]))
      weight.append(float(linha[1][:-1]))
  
  #Fechamento do arquivo
  arq.close()

  # Utilização do matplotlib para plotagem do gráfico
  plt.plot(age, weight, marker='o', markerfacecolor='white', color='k')
  
  #Definição dos valores do eixo y
  plt.yticks([2, 4, 6, 8, 10])
  
  #Definição dos labels dos eixos x e y
  plt.xlabel("Idade (meses)")
  plt.ylabel("Peso (Kg)")  
  
  #Definição do título do gráfico
  plt.title("A relação entre idade  e peso de uma criança em desenvolvimento")
  
  #Função que plota o gráfico na tela
  plt.show()

quest1()
