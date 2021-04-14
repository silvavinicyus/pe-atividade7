import matplotlib.pyplot as plt
import numpy as np
import random

def quest4():
  arq = open('dados/male_female_counts.txt', 'r')

  sample = []
  count = []

  for linha in arq:    
    linha = linha.split('\t')
    
    if('Sample' not in linha):
      sample.append(linha[0])
      count.append(int(linha[1][:-1])) 
  
  fig, ax1 = plt.subplots(figsize=(7,4))
  ax1.bar(sample, count, edgecolor='k', color=['red', 'orange', 'yellow', 'green', 'lime', 'turquoise', 'blue', 'darkblue', 'purple', 'pink'], width=0.8)
   
  plt.box(False)  
  plt.xlabel('Number of features')
  plt.tight_layout()
  plt.xticks(fontsize=8)
  plt.yticks([0, 5, 10, 15])
  plt.show()

quest4()