import numpy as np
import random

a = np.array([1,2,3],dtype=float,ndmin=1)
print(a)

b = np.array(range(10))
print(b)

c = np.arange(10)
print(c)

d = c.astype("float64")
print(d)

e = np.array([random.random() for i in range(10)])
print(e)

f = np.round(e,2)
print(f)

g = np.array([[1,2,3],[4,5,6]])
print(g.shape)

h = np.arange(24).reshape((2,3,4))
print(h)
print(h.flatten())

