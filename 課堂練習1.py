#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import matplotlib.pyplot as plt
import math
h=6.62*10**(-34)
c=3*10**8
k=1.38*10**-23
num=100
v=np.linspace(10**0, 10**15.5, num, endpoint=True)#(起點,終點,分一百點,包含終點)
T=input("input temperatures ")
B=2*h*v**3/c**2/(math.e**(h*v/k/float(T))-1)
#print(v)
#print(B)
plt.xlim(10**14, 10**15.2)
#plt.plot(v, B, "r_")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity Watt/Hz/m^2")
dB=np.random.normal(0, 10**-9, num)
B += dB
plt.plot(v,B)
plt.show()


# In[ ]:


import numpy as np
import matplotlib as plt
import math


# In[ ]:





# In[19]:


import numpy as np
import matplotlib.pyplot as plt
import math
h=6.62*10**(-34)
c=3*10**8
k=1.38*10**-23
v=np.linspace(10**0, 10**15.5, 100, endpoint=True)#(起點,終點,分一百點,包含終點)
B=2*h*v**3/c**2/(math.e**(h*v/k/5000)-1)
print(v)
print(B)
plt.xlim(10**14, 10**15.2)
plt.loglog(v, B, "r_")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Intensity Watt/Hz/m^2")

plt.show()


# In[ ]:




