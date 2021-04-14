import matplotlib.pyplot as plt
import numpy as np
import random

def quest6():  
  arq = open('dados/chromosome_position_data.txt', 'r')

  mut1 = []
  mut2 = []  
  wt = []

  for linha in arq:    
    linha = linha.split('\t')
    
    if('Position' not in linha):      
      mut1.append(float(linha[1]))
      mut2.append(float(linha[2]))
      wt.append(float(linha[3][:-1]))
  
  plt.plot(mut1, color='red')
  plt.plot(mut2, color='blue')
  plt.plot(wt, color='green')
  plt.ylabel("Value")
  plt.xlabel("Position within chromosome")
  plt.legend(['Mut1', 'Mut2', 'WT'], bbox_to_anchor=(0.2, 1), loc="upper right")
  
  plt.show()

quest6()