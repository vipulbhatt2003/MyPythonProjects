'''
Created on May 13, 2018

@author: bhattvip
'''
import os
import datetime

a=0
b=1
c=1
g=0
counter=0
print ('Fibonaaci Series and Golden Ratio - Updating the header -- Linked to Jenkins'  , file=open('C:\\Git_Testing\\Fibonaaci\\fibonacci_v4.txt', 'w') )

def nextfibonaccinumber(x,y):
    return x + y

def goldenratio(x,y):
    return y / x

while counter <= 20:
    now = datetime.datetime.now()
    #print(c,'and', g)
    print ('@Time' , str(now) , ' --> ',  c,' and Golden Ratio is', g , file=open('C:\\Git_Testing\\Fibonaaci\\fibonacci_v4.txt', 'a') )
    c=nextfibonaccinumber(a,b)
    if a > 1:
        g=goldenratio(a,b)
    a=b
    b=c
    counter += 1
