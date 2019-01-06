# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 16:45:54 2018

@author: slimc
"""
import numpy as np
import matplotlib.pyplot as plt




def Chaos_game(it,points):
    choise=[1,2,3,4]
    
    for i in range(it):
        opt=np.random.choice(choise)
    
        if opt==1:
            pos=np.dot(np.array([[0,0],[0,0.16]]).reshape(2,2),points[-1])
    
        if opt==2:
            pos=np.dot(np.array([[0.85,0.04],[-0.04,0.85]]).reshape(2,2),points[-1])+np.array([0.00,1.6])
        if opt==3:
            pos=np.dot(np.array([[0.2,-0.26],[0.23,0.22]]).reshape(2,2),points[-1])+np.array([0.00,1.6])
        if opt==4:
            pos=np.dot(np.array([[-0.15,0.28],[0.26,0.24]]).reshape(2,2),points[-1])+np.array([0.00,0.44])
        
        
        points.append(pos)
    
    plt.scatter([x[0] for x in points],[x[1] for x in points],c='g',s=1)
    return
    
    
    
        
    

#plt.scatter([0,24,12],[0,0,12],c='k')
#plt.plot([0,24,12,0],[0,0,12,0],'k',)
Chaos_game(5,[np.array([0,0])])
    