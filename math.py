import math
import sys

x=float(sys.argv [1])
y=float(sys.argv [2])
z=float(sys.argv [3])
f=(1/(z*math.sqrt(2*math.pi)))*math.exp(-(((x-y)**2)/(2*z**2)))
print f
