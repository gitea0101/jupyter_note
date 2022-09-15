#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def jegop(x, y):
    a=0
    b=0
    for i in range(x, y+1):
        a = a + i
        b = b + i**2

    return(a**2 - b)

