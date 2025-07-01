#!/usr/bin/env python
# coding: utf-8

# ## This script will fit a linear regression model to the specified data set, correlation coefficient, the mean squared error, and create a final scatter plot.

# In[1]:


# Import packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sklearn.metrics import mean_squared_error


# In[2]:


# Describe the data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 4.3, 6.1, 8.0, 10.1])


# In[3]:


# Set up linear regression
slope, intercept, r_value, p_value, std_err = linregress(x, y)
y_pred = slope * x + intercept
mse = mean_squared_error(y, y_pred)


# In[4]:


# Plot the data
plt.plot(x, y_pred, 'r-', label='Fitted Line')
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

