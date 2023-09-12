# ###################################
# Group ID : <741>
# Members : <Jon, Vasiliki, Simon>
# Date : <xx/09>
# Lecture: <3> <Parametric and nonparametric methods> (see moodle)
# Dependencies: Toolbox, library, etc. needed to run, e.g., Libsvm, netlab, LDA tool.
# Python version: Latest 3.11.2
# Functionality: Short Description. Example: This script trains a MLP for classifying
# handwritten digits. It also test the performance on a given data set for various
# settings.
# ###################################

"""
Exercise Description:

You are given, as the train data, trn_x and trn_y along with their class labels trn_x_class and trn_y_class. The task is to classify the following TEST data.
(a) classify instances in tst_xy, and use the corresponding label file tst_xy_class to calculate the accuracy;
(b) classify instances in tst_xy_126 by assuming a uniform prior over the space of hypotheses, and use the corresponding label file tst_xy_126_class to calculate the accuracy;
(c) classify instances in tst_xy_126 by assuming a prior probability of 0.9 for Class x and 0.1 for Class y, and use the corresponding label file tst_xy_126_class to calculate the accuracy; compare the results with those of (b).

To plot Gaussian, you may use PLOT_GAUSSIAN_ELLIPSOID.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def exercise_a():
    # Load trn_x_class and trn_y_class training class labels
    trn_x_class = np.loadtxt("Data/trn_x_class.txt")
    trn_y_class = np.loadtxt("Data/trn_y_class.txt")
    
    # Compute priors
    
    # Compute means, variances, covariance matrix for multivariate
    
    # Compute likelihood p(x|Ck) for test data
    
    # Compute posterior probabilities or joint probability
    
    # Calculate accuracy using labels
    
def exercise_b():
    # Load trn_x_class and trn_y_class training class labels
    trn_x_class = np.loadtxt("Data/trn_x_class.txt")
    trn_y_class = np.loadtxt("Data/trn_y_class.txt")
    
    # Compute priors
    
    # Compute means, variances, covariance matrix for multivariate
    
    # Compute likelihood p(x|Ck) for test data
    
    # Compute posterior probabilities or joint probability
    
    # Calculate accuracy using labels
    
def exercise_c():
    # Load trn_x_class and trn_y_class training class labels
    trn_x_class = np.loadtxt("Data/trn_x_class.txt")
    trn_y_class = np.loadtxt("Data/trn_y_class.txt")
    
    # Compute priors
    
    # Compute means, variances, covariance matrix for multivariate
    
    # Compute likelihood p(x|Ck) for test data
    
    # Compute posterior probabilities or joint probability
    
    # Calculate accuracy using labels
    
    

if __name__ == "__main__":
    # Exercise (a)
    exercise_a()
    
    # Exercise (b)
    exercise_b()
    
    # Exercise (c)
    exercise_c()