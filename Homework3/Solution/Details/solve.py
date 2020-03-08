import numpy as np
from math import e,pi
from scipy.linalg import solve
a = np.array([[1, 1, 1, 1], 
    [2, 1, e**(2j*pi/3),e**(-2j*pi/3)], 
    [4, 1, e**(-2j*pi/3),e**(2j*pi/3)],
    [8, 1, 1, 1]])
b = np.array([0,1,2,5])
x = solve(a, b)
print(x)
