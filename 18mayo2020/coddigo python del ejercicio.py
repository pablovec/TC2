# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:50:39 2020

@author: Pol Vecchio
"""
#%matplotlib qt5

from scipy import signal as sig
#import numpy as np
#from numpy.polynomial import Polynomial as P
from splane import bodePlot, pzmap

# $+9$^3
#poli=P([0,1,0,9])
#num_r=poli.roots()
#print("Numerador  -->",num_r)

#1+2S+2s^2+s^3
#poli2=P([9,18,18,9])
#deno_r=poli2.roots()
#print("Denominador  -->",deno_r)


#num = list(np.array([0.-0.33333333j, 0.+0.j, 0.+0.33333333j]))
#print("num: ",num)

#den = list(np.array([-1 +0j       , -0.5-0.8660254j, -0.5+0.8660254j]))
#print("dem: ",den)

#H = sig.TransferFunction( num, den )
#bodePlot(H)
#pzmap(H)

myFilter = sig.TransferFunction([9,0,1,0],[9,18,18,9])
print('Poles:',myFilter.poles)
print('Zeros:',myFilter.zeros)
bodePlot(myFilter)
pzmap(myFilter)



