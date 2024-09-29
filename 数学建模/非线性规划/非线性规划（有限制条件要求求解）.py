#使用scipy编程
from scipy.optimize import minimize
import numpy as np
def func(x):
    return 10.5+0.3*x[0]+0.32*x[1]+0.32*x[2]+0.0007*x[0]**2+0.0004*x[1]**2+0.00045*x[2]**2
cons=({'type':'eq','func':lambda x:x[0]+x[1]+x[2]-700})
b1,b2,b3=(100,200),(120,250),(150,300)
x0=np.array([100,200,400])
res=minimize(func,x0,method='BFGS',bounds=(b1,b2,b3),constraints=cons)
print(res)