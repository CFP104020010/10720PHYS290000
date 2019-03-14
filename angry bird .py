#!/usr/bin/env python
# coding: utf-8

# In[101]:


import math
import numpy as np
import matplotlib.pyplot as plt
pigx=np.random.random()*100
pigy=np.random.random()*100
v=0.1
g=9.8
deg=math.pi/8
num=1000
x=np.linspace(0, 1000, num, endpoint=True)
y=math.tan(deg)*x-(g*x**2)/(2*v**2*math.cos(deg)**2)
while pigy-(math.tan(deg)*pigx-(g*pigx**2)/(2*v**2*math.cos(deg)**2))>0.01:
    v=v+0.1
plt.plot(x, y, 'bo')
plt.plot(pigx, pigy, 'ro')
plt.show()
        
        
    
        
   

