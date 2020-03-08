import math
alpha = 5.0/7.0
beta = -2.0/3.0
gamma = -1.0/42.0-(3j*(3.0)**0.5)/42.0
delta = -1.0/42.0+(3j*(3.0)**0.5)/42.0
n = 3
# print(math.e**(2j*math.pi/3*n))
I = alpha*2.0**n + beta + gamma * math.e**(2.0j*math.pi/3.0*n) + delta*math.e**(-2.0j*math.pi/3.0*n)
# I = alpha + beta + gamma  + delta
print(I)