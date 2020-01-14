#!/usr/bin/env python
# coding: utf-8

# ## Step - 1 : Data Import

# In[7]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import math

titanic_data=pd.read_csv("titanic.csv")
titanic_data.head(10)


# In[11]:


print("Number of passengers in original data : " + str(len(titanic_data.index)))


# ## Step - 2 : Analyze Data

# ### 2.1 : Plot Survived (1) vs Non-Survived (0)

# In[14]:


sns.countplot(x="Survived", data=titanic_data)


# ###### - Above plot shows Survived and Not survived. 
# ###### - Around 550 passengers not survived and around 350 did survived.
# ###### - So there are more non survivors than survivors.

# ### 2.2 : Plot Survived (1) vs Non-Survived (0) by Sex

# In[17]:


sns.countplot(x="Survived", hue="Sex", data=titanic_data)


# ##### - Majority of Male didnot survive, where as majority of Female survived.
# ##### - Female are three times more likely to survive than male.

# ### 2.3 : Plot Survived (1) vs Non-Survived (0) by Passenger Class

# In[19]:


sns.countplot(x="Survived", hue="Pclass", data=titanic_data)


# ##### - Most of the Class-3 passengers didnot survive.
# ##### - Among survived passengers most of them belong to Class-1

# ### 2.4 : Plot Age distribution

# In[20]:


titanic_data["Age"].plot.hist()


# ##### - More pasesengers are of Mediocore age and Younger

# ### 2.5 : Plot Fare distribution

# In[23]:


titanic_data["Fare"].plot.hist(bins=20, figsize=(20,5))


# ##### - Majority of Fare is between 0 to 100

# In[ ]:




