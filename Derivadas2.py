#!/usr/bin/env python
# coding: utf-8

# # Calcular  Derivadas em python

# In[1]:


import sympy as sp
from scipy.misc import derivative


# In[2]:


# Resolvendo analiticamente
def derivate():
    x = sp.symbols('x')
    print('Atenção use * para multiplicar e ** p/ potência')
    a = input('Digite a função que deseja derivar')
    Soluction = sp.diff(a,x)
    return Soluction


# In[3]:


derivate()


# In[ ]:


#Solução numérica
 


# In[ ]:


def f(x):
    print('Atenção use * para multiplicar e ** p/ potência')
    b = input('Digite a função que deseja derivar')
    return b
print(derivative(f,2.0))   


# In[ ]:





# In[ ]:




