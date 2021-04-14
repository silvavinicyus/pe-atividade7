import matplotlib.pyplot as plt
import numpy as np
import random

def quest5():
  arq = open("dados/up_down_expression.txt", 'r')

  upx = []
  upy = []

  downx = []
  downy = []

  unchangingx = []
  unchangingy = []

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
  
  plt.scatter(upx, upy, color='red', marker='o')
  plt.scatter(unchangingx, unchangingy, color='gray', marker='o')
  plt.scatter(downx, downy, color='blue', marker='o')

  plt.xlabel("Expression C1")
  plt.ylabel("Expression C2")
  plt.yticks([0, 5, 10])
  plt.xticks([0, 5, 10])
  plt.show()

quest5()