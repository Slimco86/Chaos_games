# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:45:54 2018

@author: slimc
"""
import numpy as np
import matplotlib.pyplot as plt




def Chaos_game(it,points):
    choise=[1,2,3]
    p1=np.array([0,0])
    p2=np.array([24,0])
    p3=np.array([12,12])
    
    for i in range(it):
        opt=np.random.choice(choise)
    
        if opt==1:
            pos=(points[-1]+p1)/2
    
        if opt==2:
            pos=(points[-1]+p2)/2
        if opt==3:
            pos=(points[-1]+p3)/2
        
        points.append(pos)
    
    plt.scatter([x[0] for x in points],[x[1] for x in points],c='r')
    plt.show()
    return
    
    
    
        
    

plt.scatter([0,24,12],[0,0,12],c='k')
plt.plot([0,24,12,0],[0,0,12,0],'k',)
Chaos_game(7000,[np.array([0,0])])
    