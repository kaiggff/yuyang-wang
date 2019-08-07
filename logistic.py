
import matplotlib.pyplot as plt
import numpy as np
import math

kx = np.arange(-10, 10, 0.11)
e = math.e

def s(x):
	
	return 1 / (1 + e ** -x)
	

plt.xlabel('x', fontsize = 15)
plt.ylabel('S(x)', fontsize = 15)
#plt.title("scalar field $\phi$ v.s. x")
plt.plot(kx, s(kx))

plt.grid(True)
plt.show()