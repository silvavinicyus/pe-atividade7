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



def quest3():
  values = np.random.normal(loc=0,scale=1,size=10000)
  values2 = np.random.normal(loc=4,scale=1,size=10000)

  valuesfinal = np.concatenate((values, values2))

  plt.hist(valuesfinal, color='k', bins=110, edgecolor='k' , facecolor='white')  
  plt.box(False)
  plt.title('Mixed distribution histogram')
  plt.xlabel("Values")
  plt.ylabel('Frequency')
  plt.show()



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