import matplotlib.pyplot as plt
import numpy as np
import random

def quest1():
  arq = open('dados/weight_chart.txt', 'r')
  age = []
  weight = []  

  for linha in arq:    
    linha = linha.split('\t')
    
    if('Age' not in linha):
      age.append(int(linha[0]))
      weight.append(float(linha[1][:-1]))
  
  arq.close()

  plt.plot(age, weight, marker='o', markerfacecolor='white', color='k')
  plt.yticks([2, 4, 6, 8, 10])
  plt.xlabel("Age (months)")
  plt.ylabel("Weight (Kg)")  
  plt.title("The relationship between age and weight in a growing infant")
  plt.show()

quest1()
