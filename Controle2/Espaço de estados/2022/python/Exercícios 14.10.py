# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 09:40:12 2022

@author: Rafael
"""

from numpy import *
from matplotlib.pyplot import *
import sympy as sp

#%%

sp.init_printing()

#%%

z = sp.symbols('z')

R = (z+3)*(z+5)/((z-0.4)*(z-0.6)*(z-0.8))

A = (R*(z-0.4))
A = A.subs(z,0.4)
B = (R*(z-0.6))
B = B.subs(z,0.6)
C = (R*(z-0.8))
C = C.subs(z,0.8)

#%%

s = sp.symbols('s')
T=0.5
G = (s+4)/((s+2)*(s+5))
Gz = G.subs(s,(2/T)*(z-1)/(z+1))
Gz = sp.simplify(Gz)

