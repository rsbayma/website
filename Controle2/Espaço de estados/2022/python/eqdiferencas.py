# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 20:54:01 2022

@author: Rafael
"""

from matplotlib.pyplot import *
from numpy import *
from sympy import *

#%%

z = symbols('z')

R = (5*z+1)/(10*(z+1)*(z-0.9)*(z-0.5))

A1 = simplify(R*(z+1)).subs(z,-1)
A2 = simplify(R*(z-0.9)).subs(z,0.9)
A3 = simplify(R*(z-0.5)).subs(z,0.5)