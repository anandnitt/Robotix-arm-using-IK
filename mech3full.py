import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from math import acos,sin,radians,degrees,cos
import serial
import time
from scipy.optimize import fsolve
from scipy.interpolate import spline
import math
from math import cos,sin
import numpy as np
#from mpldatacursor import datacursor

#pylab
from matplotlib import pyplot as plt
import matplotlib.dates as mdates

g=0
h=0



def disp(a,b,t):  

    plt.plot([3.5,8.5],[8,8])
    plt.plot([6,3.5],[12.33,8])
    plt.plot([6,8.5],[12.33,8])
        
    
    x=8*cos(radians(a+b))
    y=8*sin(radians(a+b))
    
    x1=8*cos(radians(a))+x
    y1=8*sin(radians(a))+y
    #print a,b
    #print radians(a),radians(b)
    if t==-1:
        x=8*cos(radians(a))
        y=8*sin(radians(a))
    
        x1=8*cos(radians(a+b))+x
        y1=8*sin(radians(a+b))+y
    
        plt.plot([11.93,x+11.93],[0,y])
        plt.plot([x+11.93,x1+11.93],[y,y1])
    
    elif t==0:
        plt.plot([0,x],[0,y])
        plt.plot([x,x1],[y,y1])
    
    
        
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    

def calcangle(x,y,t):#x,y are coordinates
    
    h=acos((x*x+y*y-128)/128)
    g=0.5*(2*acos(x/(16*cos(h/2)))-h)
    g=degrees(g)
    h=degrees(h)
    
    #print g,h
    if t==0:
        disp(g,h,0)   # g,h are given the solution values
    else:
        disp(g,h,-1)
        
    
    
def line(x1,y1,x2,y2):
    a=deque()
    b=deque()
    
    if(x1<x2):
        i=x1
        while i<=x2:
            
            a.append(i)
            y=((y2-y1)/(x2-x1)*(i-x1))+y1
            i+=0.5
            b.append(y)
    elif(x2<x1):
        i=x1
        while i>=x2:
            
            a.append(i)
            y=((y2-y1)/(x2-x1)*(i-x1))+y1
            i-=0.5
            b.append(y)
        
    for i in xrange(0,len(a)):
        calcangle(a[i],b[i],0)
            
        

plt.ion()
#line(6,12.33,3.5,8)


line(6,12.33,3.5,8)
line(3.5,8,8.5,8)

calcangle(-6,12.33,-1)
calcangle(-5.5,11.44,-1)
calcangle(-5,10.58,-1)
calcangle(-4.5,9.72,-1)
calcangle(-4,8.86,-1)
calcangle(-3.5,8,-1)


