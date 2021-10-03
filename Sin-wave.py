import math
import matplotlib.pyplot as plot

#Set x values
x=[0]
step=(2*math.pi/100)
r=range(1,101)
for i in r:
    x=x+[i*step]


#Set y values
y=[]
for values in x:
    y=y+[math.sin(values)]

#Plot x-y graph
plot.scatter(x,y)
