import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


#Take random data from a normal distribution 

data = np.random.normal(0, 1, 1000) # mean =0, standard deviation= 1, 1000 samples

#using seaborn to plot 
sns.histplot(data, kde=True)
plt.show()