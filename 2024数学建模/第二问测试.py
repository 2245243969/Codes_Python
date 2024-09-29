import itertools
import matplotlib.pyplot as plt

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4, x5的所有组合
all_combinations = list(itertools.product(x_values, repeat=4))

valid_combinations = [comb for comb in all_combinations]

# 将算出来的L——total放入列表中，方便画图
L_total_list=[]


# 输出结果
for comb in valid_combinations:
    print(f"x1={comb[0]}, x2={comb[1]}, x3={comb[2]}, y1={comb[3]}")

    data={'p1':0.1,'p2':0.2,'p3':0.1,'b1':4,'b2':18,'c1':8,'c2':1,'c3':6,'c4':2,'c5':10,'c6':5,'r1':56}
    N=1000
    C1_buy=N/(1-data['p1']*(1-comb[0]))
    C2_buy=N/(1-data['p2']*(1-comb[1]))
    C1_text=comb[0]*N/(1-data['p1'])*data['c1']
    C2_text=comb[1]*N/(1-data['p2'])*data['c2']
    C_install=data['c3']*N
    C_finish_text=comb[2]*data['p3']*N
    p4 = (1 - data['p1'] * (1 - comb[0])) * (1 - data['p2'] * (1 - comb[1])) * (1 - data['p3'] * (1 - comb[2]))
    C_change_cost=(1-p4)*N*data['c5']
    C_disconnection_cost=comb[3]*((1-p4)*(N*data['c6']+N/(1-data['p1'])*comb[0]*data['c1']+N/(1-data['p2'])*comb[1]*data['c2'])+comb[2]*data['p3']*N*(1-p4))

    R_total=(N*(p4*(1-data['p3'])))*data['r1']

    L_total=R_total-C1_buy-C2_buy-C1_text-C2_text-C_install-C_finish_text-C_change_cost-C_disconnection_cost
    if(L_total>=0):
        L_total_list.append(L_total)
        print(L_total)
    else:
        print('0')
        L_total_list.append(0)
