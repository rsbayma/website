# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 22:08:13 2022

@author: Rafael
"""

from matplotlib.pyplot import *
from numpy import *

#%%

delta = lambda k: (k==0).astype(float)

k= linspace(start=-10,stop=10,num=21)
y = delta(k)
stem(k,y)
savefig('impulso.svg',format='svg')

#%%

x = random.normal(0,1,21)
trem = ones(x.shape)
figure()
stem(k,x)
savefig('random_x.svg',format='svg')
figure()
stem(k,trem)
savefig('trem.svg',format='svg')

#%%
degrau = lambda k: (k>=0).astype(float)
figure()
stem(k,degrau(k))
savefig('degrau.svg', format='svg')
figure()
stem(k,degrau(-k))
figure()
stem(k,degrau(k-3))
xticks(ticks=range(-10,12,2))

#%%
figure()
a = 0.9
stem(k,0.9**k * degrau(k))
savefig('exp09.svg',format='svg')
figure()
stem(k,0.6**k * degrau(k),'g')
savefig('exp06.svg',format='svg')

#%%
figure()
stem(k,1.2**k * degrau(k))
savefig('exp12.svg',format='svg')
figure()
stem(k,1.8**k * degrau(k),'g')
savefig('exp18.svg',format='svg')

#%%
w = 2*pi*0.05
k= array(range(100))
a = exp(1j*w)
x = lambda k: real(a**k * degrau(k))
figure()
stem(k,x(k))
savefig('cos.svg',format='svg')

#%%
a1 = 0.99*exp(1j*w)
x1 = lambda k: real(a1**k * degrau(k))
figure()
stem(k,x1(k))
savefig('expcos.svg',format='svg')

#%%
a2 = 1.1*exp(1j*w)
x2 = lambda k: real(a2**k * degrau(k))
figure()
stem(k,x2(k))
savefig('expcosinst.svg',format='svg')

#%%
a3 = -0.7
k= array(range(10))
x3 = lambda k: real(a3**k * degrau(k))
figure()
stem(k,x3(k))
savefig('expneg.svg',format='svg')

a4 = -1.2
k= array(range(10))
x4 = lambda k: real(a4**k * degrau(k))
figure()
stem(k,x4(k))
savefig('expneg2.svg',format='svg')

