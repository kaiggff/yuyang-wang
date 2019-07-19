import numpy as np
from matplotlib import pyplot as pl



def theta(x):
    """
    theta function :
      returns 0 if x<=0, and 1 if x>0
    """
    x = np.asarray(x)
    y = np.zeros(x.shape)
    y[x > 0] = 1.0
    return y

def square_barrier(x, width, height):
    return height * (theta(x) - theta(x - width))
	
	

	
# Set up plot
#fig = pl.figure()

# plotting limits
a = 1
V0 = 1



x = np.linspace(-0.5,1.5,100)
V = ((16 * V0) / (a ** 4)) * (x ** 2 - a * x ) ** 2
y = ((16) / (1 ** 4)) * ((( x - 1/2 ) ** 2 - (1 * 1 / 4)) ** 2) 


m= 1.4
k = V0 / ((a * m - m * m ) ** 2)

V2 = k * (x * x - m * m - a * x + a * m) ** 2


V_x = square_barrier(x, a, V0)


#pylab.plot(x,V) 
pl.plot(x,V_x)
pl.plot(x,V)
pl.plot(x,V2)
pl.show()



# y = ((16) / (1 ** 4)) * ((( x - 1/2 ) ** 2 - (1 * 1 / 4)) ** 2) 
