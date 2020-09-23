import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = pd.read_csv('./Challenge_HardworkPaysOff/TrainingData/Linear_X_Train.csv')
y = pd.read_csv('./Challenge_HardworkPaysOff/TrainingData/Linear_Y_Train.csv')

theta = np.load("ThetaList.npy")
#100,2

T0 = theta[:,0]
T1 = theta[:,1]

plt.ion() #interactive mode on
#we saw almost near 50 iterations our algorihtm gets converged (loss values keeps on changing over 50 iterations)
# we will see how our prediction line is changing with changing values of theta

# see after every 3 points
for i in range(1,50,3):
    y_ = T1[i]*X + T0[i]
    
    #points
    plt.scatter(X,y)
    
    #line
    plt.plot(X,y_,color='red')
    plt.draw() #draw the graph
    plt.pause(1) #pause the graph for 1 sec
    plt.clf() #destroy the last object
    
         
      
 #As we are getting near the minima updates are becoming slow because gradient value is decreasing