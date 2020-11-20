import numpy as np
import matplotlib.pyplot as plt

#coefficients for homework parts a)-d) in order [x_0, d, u, alpha, b, h]
coeff_a = [-1, 1, 0.31, 1.2, 0, 10**(-3)]
coeff_b = [-1, 1, 0.31, 1.2, 3, 10**(-3)]
coeff_c = [-1, 1, 0.31, 1.2, 3, 10**(-1)]
coeff_d = [-1, 4, 0.31, 1.2, 0, 10**(-3)]
coeffs = [coeff_a, coeff_b, coeff_c, coeff_d]

#define Euler algorithm for functions of type f(x,coeff)
def euler(func, coeff):
    t = np.linspace(0,7,int(7/coeff[5])+1) #coeff[5] = h
    x = np.zeros(len(t))
    x[0] = coeff[0] #coeff[0] = x_0
    for i in range(1,len(t)):
        x[i] = x[i-1] + coeff[5]*func(x[i-1], coeff)
    return x

#define dx/dt = -dx + u*tanh(alpha*x) + b
def dx_dt(x, coeff):
    return -coeff[1]*x + coeff[2]*np.tanh(coeff[3]*x) + coeff[4]

#Plotting
for coeff in coeffs:
    t = np.linspace(0,7,int(7/coeff[5]+1))
    x = euler(dx_dt, coeff)
    plt.plot(t, x)
plt.xlabel("$t$")
plt.ylabel("$x(t)$")
plt.legend(("a)", "b)", "c)", "d)"))
plt.show()
