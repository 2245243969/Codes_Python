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

# N 值固定
N = 1000

# 遍历每组数据
for data in data_sets:
    L_total_values = []  # 用于存储当前数据集的 L_total 值

    # 对每一组数据的所有组合进行运算
    for comb in valid_combinations:

        # 计算各项成本
        C1_buy = N / (1 - data['p1'] * comb[0]) * data['b1']
        C2_buy = N / (1 - data['p2'] *comb[1]) * data['b2']
        C1_text = comb[0] * N / (1 - data['p1']*comb[0]) * data['c1']
        C2_text = comb[1] * N / (1 - data['p2']*comb[1]) * data['c2']
        C_install = data['c3'] * N
        C_finish_text = comb[2] * data['p3'] * N

        # 计算合格率 p4
        p4 = (1 - data['p1'] * (1 - comb[0])) * (1 - data['p2'] * (1 - comb[1])) * (1 - data['p3'] * (1 - comb[2]))

        # 计算调换损失和拆解费用
        C_change_cost = (1 - p4) * N * (data['c5'] + data['c4'])
        C_disconnection_cost = comb[3] * (1-p4)*N*(data['c6']+comb[0]*data['c1']+comb[1]*data['c2']+comb[2]*data['c3'])
        C_buy_new_cost = (1 - comb[3]) * (1-p4)*N*(1/(1-data['p1']*comb[0])*(data['b1']+comb[0]*data['c1'])+1/(1-data['p2']*comb[1])*(data['b2']+comb[1]*data['c2'])+(data['c3']+comb[2]*data['c4']))
        # 计算总收入
        if comb[2] == 0:  # 对产品不检测
            R_total = N * data['r1']
        else:  # 对产品检测
            R_total = N * data['r1'] * p4

        # 计算总利润 L_total
        L_total = R_total - C1_buy - C2_buy - C1_text - C2_text - C_install - C_finish_text - C_change_cost - C_disconnection_cost - C_buy_new_cost

        # 如果 L_total 为正，将其存入 L_total_values
        if L_total >= 0:
            L_total_values.append(L_total)
        else:
            L_total_values.append(0)

    # 将每个 data_set 的 L_total_list 存入总列表
    L_total_list.append(L_total_values)

# 生成x轴数据，从1到16
x = list(range(1, len(valid_combinations) + 1))

# 设置不同颜色的列表，确保颜色鲜明对比
colors = ['red', 'blue', 'green', 'orange', 'purple', 'black']

# 绘制 6 条折线图
for i in range(6):
    plt.plot(x, L_total_list[i], marker='o', color=colors[i], label=f'Data Set {i + 1}')

    # 找到最高点
    max_index = np.argmax(L_total_list[i])
    max_value = L_total_list[i][max_index]

    # 标记最高点
    plt.scatter(x[max_index], max_value, color=colors[i], edgecolor='black', s=100, zorder=5)
    plt.text(x[max_index], max_value, f'  ({x[max_index]}, {max_value:.2f})', color=colors[i], fontsize=9)

# 设置 x 轴范围和刻度
plt.xticks(ticks=x, labels=x)

# 设置 x 和 y 轴范围和标签
plt.xlabel('Detection combination')
plt.ylabel('Gross profit')

# 设置图表标题
plt.title('Overall line graph for the 6 cases in question 2')

# 显示图例
plt.legend()

# 显示网格
plt.grid(True)

# 显示图表
plt.show()
