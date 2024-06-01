import numpy as np
import matplotlib.pyplot as plt

def f(x):
	return 3*x**3-2*x**2

xlist = np.linspace(-10,10,num=2001)
ylist = f(xlist)

plt.figure(num=0,dpi=120)
plt.plot(xlist,ylist)
plt.ylim(-1, 1)
plt.xlim(-1,1)
plt.grid()
plt.show()

print(xlist)
print(ylist)