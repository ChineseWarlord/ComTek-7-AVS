import numpy as np
from matplotlib import pyplot as plt

#Reading the data
classx = np.loadtxt('../Data/trn_x.txt')
classy = np.loadtxt('../Data/trn_y.txt')
targetx = np.loadtxt('../Data/trn_x_class.txt')
targety = np.loadtxt('../Data/trn_y_class.txt')


plt.scatter(classx[:, 0], classx[:, 1])
plt.scatter(classy[:, 0], classy[:, 1])

plt.show()

data = np.concatenate((classx, classy), axis = 0)
target = np.concatenate((targetx, targety), axis = 0)
