#!/usr/bin/env python
# coding: utf-8

# ## This script will fit a linear regression model to the specified data set, correlation coefficient, the mean squared error, and create a final scatter plot.

# In[1]:


# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error
import pandas as pd
import sys


# In[2]:


# Load in the data
if len(sys.argv) != 4:
    print("Usage: python linear_regression_python.py <filename> <x_column> <y_column>")
    sys.exit(1)

filename = sys.argv[1]
x_col = sys.argv[2]
y_col = sys.argv[3]

df = pd.read_csv(filename)

# In[3]:
# Describe the data
x = df[x_col].to_numpy()
y = df[y_col].to_numpy()

# Set up linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)


# In[4]:


# Plot the data
plt.plot(x, y_pred, 'r-', label='Fitted Line')
plt.scatter(df[[x_col]], df[[y_col]], color='red')
plt.text(1.5, max(y) - 1,
         f"y = {slope:.2f}x + {intercept:.2f}\n"
         f"r = {r_value:.2f}\nMSE = {mse:.2f}",
         fontsize=12)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Regression")
plt.legend()
plt.savefig("regression_plot_python.png")
plt.show()


# In[ ]:


#hooray :)

