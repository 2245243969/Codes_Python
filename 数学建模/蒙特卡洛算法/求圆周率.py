import numpy as np
import matplotlib.pyplot as plt

#参数初始化，投掷100000个点，圆的半径为1，圆心坐标为（1，1）
p = 100000#总共投掷的个数
r=1#圆的半径
x0,y0=1,1
n=0#初始还未投掷点，有0个点在圆内

#设置绘图窗口
plt.figure()
plt.title('Monte Carlo Simulation for Estimating Pi')
plt.xlabel('x')
plt.ylabel('y')

#保持绘图窗口，多次绘图
for i in range(p):
    px=np.random.rand()*2
    py=np.random.rand()*2

    #判断点是否在圆内
    if(px-x0)**2+(py-y0)**2<r**2:
        plt.plot(px,py,'.',color='b')
        n+=1
    else:
        plt.plot(px,py,'.',color='r')

plt.axis('equal')#绘图时横纵坐标单位长度相同，便于观察圆
plt.show()

#计算Π的估算值
s=(n/p)*4
pi_estimate=s
print('Estimated value of Π:',pi_estimate)