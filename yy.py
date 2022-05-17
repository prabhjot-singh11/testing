import  matplotlib.pyplot as plt
import numpy as np
mylabels=["red","green","yellow","blue"]
y= np.array([30,30,20,20])
myexploode = [.1,.1,.1,.1]
plt.pie(y,labels=mylabels,explode=myexploode)
plt.show()
