# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:05:30 2022

@author: Rafael
"""

from control import *
from matplotlib import pyplot as plt
import numpy as np

#%%
t1 = np.linspace(0, 1,50)
t2 = np.linspace(0, 1,200)
t3 = np.linspace(0, 1,500)
f=2
y1 = np.cos(2*np.pi*f*t1)
y2 = np.cos(2*np.pi*f*t2)
y3 = np.cos(2*np.pi*f*t3)
plt.plot(t3,y3)
plt.savefig('continuo.svg', format='svg')
plt.figure()
plt.plot(t1,y1,'or',t2,y2,'xb')
p = plt.gcf()
plt.grid()
plt.xlim([0, 0.1])
p.savefig('teste.svg',format='svg')


#%%
from numpy.fft import fft, ifft
f = 1
T = 20/f
f1 = 10
f2 = 8
f3 = 5
N1 = np.round(f1*T)
N2 = np.round(f2*T)
N3 = np.round(f3*T)

t = np.linspace(0, T,500)
x = np.cos(2*np.pi*f*t)
t1 = np.linspace(0,T,int(N1))
x1 = np.cos(2*np.pi*f*t1)
t2 = np.linspace(0,T,int(N2))
x2 = np.cos(2*np.pi*f*t2)
t3 = np.linspace(0,T,int(N3))
x3 = np.cos(2*np.pi*f*t3)

plt.plot(t,x,t1,x1,'or--')
plt.figure()
plt.plot(t,x,t2,x2,'or--')
plt.figure()
plt.plot(t,x,t3,x3,'or--')