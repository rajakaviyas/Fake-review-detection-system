import os
import base64
import io
from plotly import graph_objects as go

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

f11=open("static/det1.txt","r")
rk=f11.read()
f11.close()
rk1=rk.split('|')
    
#
y=[]
x1=[]
x2=[]



x1=rk1[0].split(',')
y=rk1[4].split(',')
x2=rk1[1].split(',')

print(y)

# plotting multiple lines from array
plt.plot(y,x1)
plt.plot(y,x2)

dd=["Training","Validation"]
plt.legend(dd)
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.title("")


fn="acc1.png"

plt.savefig('static/graph/'+fn)
#plt.close()
plt.clf()
####
'''y=[]
x1=[]
x2=[]



x1=rk1[2].split(',')
y=rk1[4].split(',')
x2=rk1[3].split(',')


# plotting multiple lines from array
plt.plot(y,x1)
plt.plot(y,x2)
dd=["Training","Validation"]
plt.legend(dd)
plt.xlabel("Epochs")
plt.ylabel("Accuracy")
plt.title("")


fn="acc2.png"

plt.savefig('static/graph/'+fn)
#plt.close()
plt.clf()'''
