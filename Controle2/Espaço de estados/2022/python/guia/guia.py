# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 17:50:30 2022

@author: Rafael
"""

import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt
#%%

w = np.linspace(0,2*np.pi,num=200);
z = np.exp(1j*w*1)
plt.plot(np.real(z),np.imag(z))
plt.axis('equal')
plt.grid()
plt.savefig('circulo.eps',format='eps')

#%%

plt.figure()
fig,ax = plt.subplots()
from matplotlib.patches import Circle

c=Circle((0,0),radius=1,color='red')
ax.add_patch(c)
plt.axis([-1,1,-1,1])
plt.axis('equal')
plt.show()

#%% Exponencial pura estável, não-alternante

a=0.8
x = lambda k: (a)**k * (k>=0)
k = np.arange(20)


plt.figure()
plt.plot(np.real(z),np.imag(z))
plt.plot([a],[0.],'xk')
plt.axis('equal')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.yticks(ticks=[-1,0,1])
plt.xticks(ticks=[-1,0,1])
plt.grid()
plt.show()

plt.figure()
plt.stem(k,x(k))
plt.xticks(ticks=k[range(0,20,2)])

#%% Exponencial pura estável, alternante
a=-0.8
x = lambda k: (a)**k * (k>=0)
k = np.arange(20)

plt.close('all')
plt.figure()
plt.plot(np.real(z),np.imag(z))
plt.plot([a],[0.],'xk')
plt.axis('equal')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.yticks(ticks=[-1,0,1])
plt.xticks(ticks=[-1,0,1])
plt.grid()
plt.show()

plt.figure()
plt.stem(k,x(k))
plt.xticks(ticks=k[range(0,20,2)])

#%% Exponencial pura instável, não-alternante
a=1.3
x = lambda k: (a)**k * (k>=0)
k = np.arange(20)

plt.close('all')
plt.figure()
plt.plot(np.real(z),np.imag(z))
plt.plot([a],[0.],'xk')
plt.axis('equal')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.yticks(ticks=[-1,0,1])
plt.xticks(ticks=[-1,0,1])
plt.grid()
plt.show()

plt.figure()
plt.stem(k,x(k))
plt.xticks(ticks=k[range(0,20,2)])

#%% Exponencial pura estável, alternante
a=-1.3
x = lambda k: (a)**k * (k>=0)
k = np.arange(20)

plt.close('all')
plt.figure()
plt.plot(np.real(z),np.imag(z))
plt.plot([a],[0.],'xk')
plt.axis('equal')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.yticks(ticks=[-1,0,1])
plt.xticks(ticks=[-1,0,1])
plt.grid()
plt.show()

plt.figure()
plt.stem(k,x(k))
plt.xticks(ticks=k[range(0,20,2)])

#%% Degray
a=1
x = lambda k:  (k>=0)
k = np.arange(start=-3,stop=20,step=1)

plt.close('all')
plt.figure()
plt.plot(np.real(z),np.imag(z))
plt.plot([a],[0.],'xk')
plt.axis('equal')
plt.axis([-1.1,1.1,-1.1,1.1])
plt.yticks(ticks=[-1,0,1])
plt.xticks(ticks=[-1,0,1])
plt.grid()
plt.show()

plt.figure()
plt.stem(k,x(k))
plt.xticks(ticks=k[range(0,20,2)])