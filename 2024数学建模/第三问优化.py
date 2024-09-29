import itertools
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import norm

# 定义参数
p0 = 0.10  # 标称次品率
delta = 0.03  # 容许的误差幅度

# 显著性水平和对应的Z值
alpha_95 = 0.05
alpha_90 = 0.10
z_95 = norm.ppf(1 - alpha_95 / 2)  # 双边检验的Z值
z_90 = norm.ppf(1 - alpha_90 / 2)  # 双边检验的Z值

# 计算样本量的函数
def calculate_min_sample_size(z_a, p0, delta):
    return math.ceil((z_a**2 * p0 * (1 - p0)) / delta**2)

# 计算样本量
n_95 = calculate_min_sample_size(z_95, p0, delta)
n_90 = calculate_min_sample_size(z_90, p0, delta)

print(f"在95%的信度下，所需的最小样本量为: {n_95}")
print(f"在90%的信度下，所需的最小样本量为: {n_90}")

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=16))
valid_combinations = [comb for comb in all_combinations]

# 数据集
data = {'e1': 2, 'e2': 8, 'e3': 12, 'e4': 2, 'e5': 8, 'e6': 12, 'e7': 8, 'e8': 12,
        't1': 1, 't2': 1, 't3': 2, 't4': 1, 't5': 1, 't6': 2, 't7': 1, 't8': 2, 't9': 4, 't10': 4, 't11': 4, 't12': 6,
        'd1': 8, 'd2': 8, 'd3': 8, 'd4': 8, 'd5': 40,
        'h1': 6, 'h2': 6, 'h3': 6, 'h4': 10,
        'r2': 200,
        'p1': 0.1, 'p2': 0.1, 'p3': 0.1, 'p4': 0.1, 'p5': 0.1, 'p6': 0.1, 'p7': 0.1, 'p8': 0.1}

# 开始购入零件1~8的数量
N1 = 1000
N2 = 1000
N3 = 1000
N4 = 1000
N5 = 1000
N6 = 1000
N7 = 1000
N8 = 1000

L_total_set = []

# 遍历组合并进行计算
for comb in valid_combinations:
    """对所有组合进行运算"""

    # 样本量和次品率的估计 (抽样检测零件1-8)
    n_sample = n_95  # 使用95%信度下的样本量
    estimated_defect_rates = []  # 存储每个零件的次品率

    for i in range(8):  # 对每个零件进行抽样检测
        p = data[f'p{i+1}']
        detected_defects = np.random.binomial(n=n_sample, p=p)  # 模拟抽样检测次品率
        estimated_defect_rate = detected_defects / n_sample  # 推测出的次品率
        estimated_defect_rates.append(estimated_defect_rate)  # 存入估计的次品率

    # 根据抽样检测结果决定是否进行全面检测
    N1_into_semi_pro = (1 - estimated_defect_rates[0]) * N1 if comb[0] == 1 else N1
    N2_into_semi_pro = (1 - estimated_defect_rates[1]) * N2 if comb[1] == 1 else N2
    N3_into_semi_pro = (1 - estimated_defect_rates[2]) * N3 if comb[2] == 1 else N3
    N4_into_semi_pro = (1 - estimated_defect_rates[3]) * N4 if comb[3] == 1 else N4
    N5_into_semi_pro = (1 - estimated_defect_rates[4]) * N5 if comb[4] == 1 else N5
    N6_into_semi_pro = (1 - estimated_defect_rates[5]) * N6 if comb[5] == 1 else N6
    N7_into_semi_pro = (1 - estimated_defect_rates[6]) * N7 if comb[6] == 1 else N7
    N8_into_semi_pro = (1 - estimated_defect_rates[7]) * N8 if comb[7] == 1 else N8

    # 求零件1-8的购买价格和检测成本之和
    C_buy_and_text_parts = N1_into_semi_pro * data['e1'] + N2_into_semi_pro * data['e2'] + N3_into_semi_pro * data['e3'] + N4_into_semi_pro * data['e4']
    C_buy_and_text_parts += N5_into_semi_pro * data['e5'] + N6_into_semi_pro * data['e6'] + N7_into_semi_pro * data['e7'] + N8_into_semi_pro * data['e8']
    C_buy_and_text_parts += comb[0] * N1_into_semi_pro * data['t1'] + comb[1] * N2_into_semi_pro * data['t2'] + comb[2] * N3_into_semi_pro * data['t3'] + comb[3] * N4_into_semi_pro * data['t4']
    C_buy_and_text_parts += comb[4] * N5_into_semi_pro * data['t5'] + comb[5] * N6_into_semi_pro * data['t6'] + comb[6] * N7_into_semi_pro * data['t7'] + comb[7] * N8_into_semi_pro * data['t8']

    # 装配半成品
    N1_finish_install = min(N1_into_semi_pro, N2_into_semi_pro, N3_into_semi_pro)
    N2_finish_install = min(N4_into_semi_pro, N5_into_semi_pro, N6_into_semi_pro)
    N3_finish_install = min(N7_into_semi_pro, N8_into_semi_pro)

    # 半成品1-3总废品率估计（通过抽样检测动态计算次品率）
    def sample_semi_pro_defect_rate(part_defect_rates, sample_size, comb_flag):
        # 先估计次品率，若组合指定进行检测，则基于抽样更新次品率
        combined_defect_rate = 1 - np.prod([1 - rate for rate in part_defect_rates])
        if comb_flag == 1:
            detected_defects = np.random.binomial(n=sample_size, p=combined_defect_rate)
            combined_defect_rate = detected_defects / sample_size
        return combined_defect_rate

    # 半成品1、2、3的次品率（根据组合情况是否抽样检测）
    p1_semi_pro_bad = sample_semi_pro_defect_rate(
        [estimated_defect_rates[0], estimated_defect_rates[1], estimated_defect_rates[2]], n_sample, comb[8])
    p2_semi_pro_bad = sample_semi_pro_defect_rate(
        [estimated_defect_rates[3], estimated_defect_rates[4], estimated_defect_rates[5]], n_sample, comb[9])
    p3_semi_pro_bad = sample_semi_pro_defect_rate(
        [estimated_defect_rates[6], estimated_defect_rates[7]], n_sample, comb[10])

    # 半成品1-3进入组装成品分别的个数
    N1_into_pro = (1 - p1_semi_pro_bad) * N1_finish_install if comb[8] == 1 else N1_finish_install
    N2_into_pro = (1 - p2_semi_pro_bad) * N2_finish_install if comb[9] == 1 else N2_finish_install
    N3_into_pro = (1 - p3_semi_pro_bad) * N3_finish_install if comb[10] == 1 else N3_finish_install

    # 组装出来的成品总数
    N_pro_total = min(N1_into_pro, N2_into_pro, N3_into_pro)

    # 成品的销售额
    R_pro_sell = N_pro_total * data['r2']

    # 成品中的总次品率
    if (comb[8] + comb[9] + comb[10] == 3):  # 对半成品1-3都检验
        p_pro_bad = 0.1
    elif (comb[8] + comb[9] + comb[10] == 2):  # 检测两个
        if comb[8] == 0:
            p_pro_bad = p1_semi_pro_bad
        elif comb[9] == 0:
            p_pro_bad = p2_semi_pro_bad
        else:
            p_pro_bad = p3_semi_pro_bad
    elif (comb[8] + comb[9] + comb[10] == 1):  # 只检测一个
        p_pro_bad = max(p1_semi_pro_bad, p2_semi_pro_bad, p3_semi_pro_bad)
    else:  # 全部不检测
        p_pro_bad = (p1_semi_pro_bad + p2_semi_pro_bad + p3_semi_pro_bad) / 3

    # 成品中的次品数量
    N_bad_in_pro = N_pro_total * p_pro_bad

    # 生产成品的装配成本和检测成本之和
    C_install_pro_total = N_pro_total * data['d4'] + comb[14] * N_pro_total * data['t12']

    # 调换损失和拆解费用
    C_exchange = (1 - comb[14]) * N_bad_in_pro * data['d5']
    C_disconnect_pro = comb[15] * N_bad_in_pro * data['h4']
    C_exchange_new_pro = (1 - comb[14]) * N_bad_in_pro * data['r2']

    # 成品中的次品所带来的成本
    C_pro_bad_total = C_exchange + C_disconnect_pro + C_exchange_new_pro

    # 计算总利润
    L_total = R_pro_sell - C_buy_and_text_parts - C_install_pro_total - C_pro_bad_total
    if L_total >= 0:
        L_total_set.append(L_total)
    else:
        L_total_set.append(0)

# 找到最大值
max_value = max(L_total_set)
max_index = L_total_set.index(max_value)

# 输出最大利润对应的组合
print(f"最大总利润为: {max_value}")
print(f"对应的组合是: {valid_combinations[max_index]}")

# 绘制折线图
plt.figure(figsize=(10, 6))
plt.plot(range(len(L_total_set)), L_total_set, label="L_total values", color='blue')

# 标记最大利润的点
plt.scatter(max_index, max_value, color='red', label=f"Max Profit: {max_value}", zorder=5)

# 添加标题和标签
plt.title("Total Profit for Different Combinations", fontsize=16)
plt.xlabel("Combination Index", fontsize=12)
plt.ylabel("Total Profit (L_total)", fontsize=12)
plt.legend()
plt.grid(True)

# 显示折线图
plt.show()
