import matplotlib.pyplot as plt
import numpy as np
import random

def quest2():
  arq = open('dados/feature_counts.txt', 'r')

  feature = []
  count = []

  for linha in arq:    
    linha = linha.split('\t')
    
    if('Feature' not in linha):
      feature.append(linha[0])
      count.append(int(linha[1][:-1])) 
  
  fig, ax1 = plt.subplots(figsize=(6,5))
  ax1.barh(feature, count, edgecolor='k', facecolor='gray')
   
  plt.box(False)  
  plt.xticks([0, 20000, 40000, 60000])
  plt.xlabel('Number of features')
  plt.tight_layout()
  plt.show()

quest2()