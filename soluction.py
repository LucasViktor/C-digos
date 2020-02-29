#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sympy import *

#Definindo um símblo para variável
x = symbols('x')

#Deixando o usuário definir a equação
def Soluction():
    print('Atenção! use ** para representar potências')
    print('Escreva apenas a parte a esquerda da equação')
    print('Exemplo: 2*x**2-2*x-1')
    a = input('Digite a equação que você deseja resolver:')
    result = solve(a,x)
    return result


# In[2]:


Soluction()


# In[ ]:




