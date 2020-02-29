#!/usr/bin/env python
# coding: utf-8

# #Integration 

# In[1]:


#Analytical Soluction 
import sympy as sp
x = sp.symbols('x')
sp.integrate(3*x**2+1,x)


# In[3]:


#numerica
from scipy.integrate import quad
def f(x):
    return 3*x**2+1*x
i ,r = quad(f,0,2)
print (i)


# In[ ]:





# In[ ]:




