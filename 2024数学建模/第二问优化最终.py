import itertools
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm

# 定义计算样本量的函数
def calculate_min_sample_size(z_a, p0, delta):
    return math.ceil((z_a**2 * p0 * (1 - p0)) / delta**2)

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=4))
valid_combinations = [comb for comb in all_combinations]

L_total_list=[]

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
# N 值固定
N = 1000

# 显著性水平和对应的Z值
alpha_95 = 0.05
z_95 = norm.ppf(1 - alpha_95 / 2)  # 双边检验的Z值

# 容许误差
delta = 0.03

for data in data_sets:
    L_total_values = []


    for comb in valid_combinations:

        n_sample_1 = calculate_min_sample_size(z_95, data['p1'], delta)
        n_sample_2 = calculate_min_sample_size(z_95, data['p2'], delta)


        detected_defects_1 = np.random.binomial(n=n_sample_1, p=data['p1'])  # 模拟抽样检测
        detected_defects_2 = np.random.binomial(n=n_sample_2, p=data['p2'])

        estimated_defect_rate_1 = detected_defects_1 / n_sample_1  # 抽样推测的次品率1
        estimated_defect_rate_2 = detected_defects_2 / n_sample_2  # 抽样推测的次品率2

        # 基于抽样检测的次品率来决定是否进行全面检测
        if estimated_defect_rate_1 > 0.1:  # 如果次品率高于10%，则进行全面检测
            C1_text = comb[0] * N / (1 - data['p1'] * comb[0]) * data['c1']
        else:
            C1_text = 0  # 次品率较低时，不进行全面检测

        if estimated_defect_rate_2 > 0.1:
            C2_text = comb[1] * N / (1 - data['p2'] * comb[1]) * data['c2']
        else:
            C2_text = 0


        C1_buy = N / (1 - data['p1'] * comb[0]) * data['b1']
        C2_buy = N / (1 - data['p2'] * comb[1]) * data['b2']
        C_install = data['c3'] * N
        C_finish_text = comb[2] * data['p3'] * N

        p4 = (1 - data['p1'] * (1 - comb[0])) * (1 - data['p2'] * (1 - comb[1])) * (1 - data['p3'] * (1 - comb[2]))

        C_change_cost = (1 - p4) * N * (data['c5'] + data['c4'])
        C_disconnection_cost = comb[3] * (1-p4)*N*(data['c6']+comb[0]*data['c1']+comb[1]*data['c2']+comb[2]*data['c3'])
        C_buy_new_cost = (1 - comb[3]) * (1-p4)*N*(1/(1-data['p1']*comb[0])*(data['b1']+comb[0]*data['c1'])+1/(1-data['p2']*comb[1])*(data['b2']+comb[1]*data['c2'])+(data['c3']+comb[2]*data['c4']))

        R_total = N * data['r1'] * p4 if comb[2] == 1 else N * data['r1']

        L_total = R_total - C1_buy - C2_buy - C1_text - C2_text - C_install - C_finish_text - C_change_cost - C_disconnection_cost - C_buy_new_cost

        L_total_values.append(max(L_total, 0))

    # 存储结果，后续可以用于绘图
    L_total_list.append(L_total_values)

# 生成x轴数据，从1到16
x = list(range(1, len(valid_combinations) + 1))

# 绘制图表
colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']
for i in range(len(L_total_list)):
    plt.plot(x, L_total_list[i], marker='o', color=colors[i], label=f'Data Set {i + 1}')
    max_index = np.argmax(L_total_list[i])
    max_value = L_total_list[i][max_index]
    plt.scatter(x[max_index], max_value, color=colors[i], edgecolor='black', s=100, zorder=5)
    plt.text(x[max_index], max_value, f'  ({x[max_index]}, {max_value:.2f})', color=colors[i], fontsize=9)

# 设置图表属性
plt.xticks(ticks=x, labels=x)
plt.xlabel('Detection combination')
plt.ylabel('Gross profit')
plt.title('Overall line graph for the 6 cases in question 2')
plt.legend()
plt.grid(True)
plt.show()
