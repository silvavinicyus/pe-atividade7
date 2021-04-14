import matplotlib.pyplot as plt
import numpy as np
import random

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

quest3()