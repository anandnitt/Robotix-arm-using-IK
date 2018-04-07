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
from matplotlib import pyplot as plt
#import matplotlib.dates as mdates

g=0
h=0

def equations(p):
    x,y = p
    f1 = (10*cos(math.radians(x))+5*cos(math.radians(x+y))-g)
    f2=(10*sin(math.radians(x))+5*sin(math.radians(x+y))-h)
    return (f1,f2)

def disp(a,b,t):  

    plt.plot([7.5,5],[12.33,8])
    plt.plot([5,10],[8,8])
    plt.plot([7.5,10],[12.33,8])
        
    x=10*cos(radians(a))
    y=10*sin(radians(a))
    
    x1=5*cos(radians(a+b))+x
    y1=5*sin(radians(a+b))+y
    #print a,b
    #print radians(a),radians(b)
    if t==-1:
        plt.plot([14.93,x+14.93],[0,y])
        plt.plot([x+14.93,x1+14.93],[y,y1])
    
    elif t==0:
        plt.plot([0,x],[0,y])
        plt.plot([x,x1],[y,y1])
    
    
        
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    

def calcangle(x,y,t):#x,y are coordinates
    
    global g,h
    g=x     #g is angle1
    h=y     #h is angle 2
    o,p=fsolve(equations,(0,0))
    #print g,h
    if t==0:
        disp(o,p,0)   # g,h are given the solution values
    else:
        disp(o,p,-1)
        
    
    
def line(x1,y1,x2,y2):
    a=deque()
    b=deque()
    
    if(x1<x2):
        i=x1
        while i<=x2:
            i+=0.2
            a.append(i)
            y=((y2-y1)/(x2-x1)*(i-x1))+y1
            
            b.append(y)
    elif(x2<x1):
        i=x2
        while i<=x1:
            i+=0.2
            a.append(i)
            y=((y2-y1)/(x2-x1)*(i-x1))+y1
            b.append(y)
        
    for i in xrange(0,len(a)):
        calcangle(a[i],b[i],0)
        #print a[i],b[i]
            
        

plt.ion()






line(5,8,7.5,12.33)
line(5,8,10,8)

#for second side



calcangle(-7.5,12.33,-1)
calcangle(-7,11.44,-1)
calcangle(-6.5,10.58,-1)
calcangle(-6,9.72,-1)
calcangle(-5.5,8.86,-1)
calcangle(-5,8,-1)







