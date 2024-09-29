import itertools
import matplotlib.pyplot as plt
import numpy as np

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=4))
valid_combinations = [comb for comb in all_combinations]

# 多组 data，每组数据都包括 p1, p2, p3 等参数
data_sets = [
    {'p1': 0.1, 'p2': 0.1, 'p3': 0.1, 'b1': 4, 'b2': 18, 'c1': 2, 'c2': 3, 'c3': 6, 'c4': 3, 'c5': 6, 'c6': 5,
     'r1': 56},
    {'p1': 0.2, 'p2': 0.2, 'p3': 0.2, 'b1': 4, 'b2': 18, 'c1': 2, 'c2': 3, 'c3': 6, 'c4': 3, 'c5': 6, 'c6': 5,
     'r1': 56},
    {'p1': 0.1, 'p2': 0.1, 'p3': 0.1, 'b1': 4, 'b2': 18, 'c1': 2, 'c2': 3, 'c3': 6, 'c4': 3, 'c5': 30,
     'c6': 5, 'r1': 56},
    {'p1': 0.2, 'p2': 0.2, 'p3': 0.2, 'b1': 4, 'b2': 18, 'c1': 1, 'c2': 1, 'c3': 6, 'c4': 2, 'c5': 30,
     'c6': 5, 'r1': 56},
    {'p1': 0.1, 'p2': 0.2, 'p3': 0.1, 'b1': 4, 'b2': 18, 'c1': 8, 'c2': 1, 'c3': 6, 'c4': 2, 'c5': 10,
     'c6': 5, 'r1': 56},
    {'p1': 0.05, 'p2': 0.05, 'p3': 0.05, 'b1': 4, 'b2': 18, 'c1': 2, 'c2': 3, 'c3': 6, 'c4': 3, 'c5': 10, 'c6': 40,
     'r1': 56}
]

# 将每一次生成的 L_total 存入 L_total_list 中
L_total_list = []

# 设购入10000零件1，10000零件2
N1_buy = 10000
N2_buy=10000

# 遍历每组数据
for data in data_sets:
    L_total_values = []  # 用于存储当前数据集的 L_total 值

    # 对每一组数据的所有组合进行运算
    for comb in valid_combinations:
        #求能组装的成品数N_finish
        if(comb[0]==1):
            N1_buy_install=(1-data['p1'])*N1_buy
        else:
            N1_buy_install=N1_buy

        if(comb[1]==1):
            N2_buy_install=(1-data['p2'])*N2_buy
        else:
            N2_buy_install=N2_buy

        N_finish=min(N1_buy_install,N2_buy_install)

        #求零件1的总成本，购买和检测
        C1_total=N1_buy*data['b1']+N1_buy*data['c1']*comb[0]

        #求零件2的总成本，购买和检测
        C2_total=N2_buy*data['b2']+N2_buy*data['c2']*comb[1]

        # 求成品的总成本，组装和检测
        C_finish_total=N_finish*data['c3']+N_finish*data['c4']*comb[2]

        # 计算零件1，零件2和成品次品率求出的成品合格率 p4
        if(comb[0]==1 and comb[1]==1):
            p4=(1-data['p3'])
        if (comb[0] == 1 and comb[1] == 0):
            p4=(1-data['p2']-(1-data['p2'])*data['p3'])
        if (comb[0] == 0 and comb[1] == 1):
            p4 = (1 - data['p1'] - (1 - data['p1']) * data['p3'])
        if (comb[0] == 0 and comb[1] == 0):
            p4=(1-data['p1'])*(1-data['p2'])*(1-data['p3'])

        #次品的个数
        N_bad=N_finish*(1-p4)

        #次品成本为赔偿成本+调换成本+拆解成本
        C_bad_total=N_bad*data['r1']+N_bad*data['c5']+comb[3]*N_bad*data['c6']

        #销售利润
        R_sell=N_finish*data['r1']

        #拆解出来的好的零件1和好的零件二数量
        if(comb[0]==1 and comb[1]==1):
            N_disconnect=data['p3']*N_finish
            N_disconnect_good_1=N_disconnect
            N_disconnect_good_2 = N_disconnect

        if(comb[0]==1 and comb[1]==0):
            N_disconnect=data['p3']*N_finish*(1-data['p2'])+N_finish*data['p2']
            N_disconnect_good_1=N_disconnect
            N_disconnect_good_2=data['p3']*N_finish*(1-data['p2'])

        if(comb[0]==0 and comb[1]==1):
            N_disconnect=data['p3']*N_finish*(1-data['p1'])+N_finish*data['p1']
            N_disconnect_good_2=N_disconnect
            N_disconnect_good_1=data['p3']*N_finish*(1-data['p1'])

        if(comb[0]==0 and comb[1]==0):
            N_disconnect=N_finish*(data['p1']+data['p2']-data['p1']*data['p2']+(1-data['p1'])*(1-data['p2'])*data['p3'])
            N_disconnect_good_1=N_disconnect*((1-data['p1'])*data['p2']+(1-data['p1'])*(1-data['p2'])*data['p3'])
            N_disconnect_good_2=N_disconnect*((1-data['p2'])*data['p1']+(1-data['p1'])*(1-data['p2'])*data['p3'])


        #拆卸带来的收益
        R_disconnect=comb[3]*(data['b1']*N_disconnect_good_1+data['b2']*N_disconnect_good_2)

        #总利润
        L_total=R_sell+R_disconnect-C1_total-C2_total-C_finish_total-C_bad_total

        # 如果 L_total 为正，将其存入 L_total_values
        if L_total >= 0:
            L_total_values.append(L_total)
        else:
            L_total_values.append(0)

    # 将每个 data_set 的 L_total_list 存入总列表
    L_total_list.append(L_total_values)

x = list(range(1, len(valid_combinations) + 1))
print(L_total_list)

colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

# 绘制 6 条折线图
for i in range(6):
    plt.plot(x, L_total_list[i], marker='o', color=colors[i], label=f'Data Set {i + 1}')

    max_index = np.argmax(L_total_list[i])
    max_value = L_total_list[i][max_index]

    plt.scatter(x[max_index], max_value, color=colors[i], edgecolor='black', s=100, zorder=5)
    plt.text(x[max_index], max_value, f'  ({x[max_index]}, {max_value:.2f})', color=colors[i], fontsize=9)

plt.xticks(ticks=x, labels=x)

plt.xlabel('Detection combination')
plt.ylabel('Gross profit')

plt.title('Overall line graph for the 6 cases in question 2')

plt.legend()

plt.grid(True)

plt.show()
