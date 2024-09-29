import cvxpy as cp
import numpy as np
c=np.loadtxt()#需要填入表的数据的文件，.txt
x=cp.Variable((4,5),integer=True)
obj=cp.Minimize(cp.sum(cp.multiply(c,x)))
cons=[0<=x,x<=1,cp.sum(x,axis=0)==1,
      cp.sum(x,axis=1)<=2]
prob=cp.Problem(obj,cons)
prob.solve(solver='GLPK_MI')
print('最优解为：',x.value)
print('最优值为：',prob.value)