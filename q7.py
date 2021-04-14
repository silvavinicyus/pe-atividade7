import matplotlib.pyplot as plt
import numpy as np
import random

def quest7():
  arq = open('dados/brain_bodyweight.txt', 'r')

  for linha in arq:
    linha = linha.split('\t')

    if ('Bodyweight ' not in linha):      
      yposition = float(linha[1])
      xposition = float(linha[2])

      xerror = float(linha[4])
      yerror = float(linha[3])

      text = str(linha[0])      

      plt.errorbar(xposition, yposition, yerr=yerror, xerr=xerror, color='black', marker='d', capsize=4)
      plt.text((xposition-0.15), (yposition-0.3), s=text,fontdict=dict(size=6))  
  
  plt.xlabel('Brain Weight')
  plt.yticks([-1, 0, 1, 2, 3, 4, 5])
  plt.xticks([0, 1, 2, 3])
  plt.ylabel('Body Weight')
  plt.show()
  
quest7()