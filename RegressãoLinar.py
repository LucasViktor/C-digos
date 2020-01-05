#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt


# In[10]:


from sklearn.linear_model import LinearRegression
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')


# In[17]:


X=[[2],[3],[4],[4],[7]]


# In[16]:


Y=[[2],[3],[5],[6],[7]]


# In[15]:


modelo=LinearRegression()


# In[7]:


#treinando


# In[18]:


modelo.fit(X,Y)


# In[23]:


plt.scatter(X,Y, color='blue')
plt.plot(X, modelo.predict(X), color='red', linewidth=3)
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(())
plt.yticks(())
plt.show()


# In[ ]:





# In[ ]:




