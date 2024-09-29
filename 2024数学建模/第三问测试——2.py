import itertools
import matplotlib.pyplot as plt
import numpy as np

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=16))
valid_combinations = [comb for comb in all_combinations]
print(valid_combinations)

# 数据集
data = {'e1': 2, 'e2': 8, 'e3': 12, 'e4': 2, 'e5': 8, 'e6': 12, 'e7': 8, 'e8': 12,
        't1': 1, 't2': 1, 't3': 2, 't4': 1, 't5': 1, 't6': 2, 't7': 1, 't8': 2, 't9': 4, 't10': 4, 't11': 4, 't12': 6,
        'd1': 8, 'd2': 8, 'd3': 8, 'd4': 8, 'd5': 40,
        'h1': 6, 'h2': 6, 'h3': 6, 'h4': 10,
        'r2': 200,
        'p1': 0.1, 'p2': 0.1, 'p3': 0.1, 'p4': 0.1, 'p5': 0.1, 'p6': 0.1, 'p7': 0.1, 'p8': 0.1, 'p9': 0.1, 'p10': 0.1,
        'p11': 0.1, 'p12': 0.1}

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
comb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

# 求购买的零件1-8分别进入装配半成品的数目
if (comb[0] == 1):
    N1_into_semi_pro = (1 - data['p1']) * N1
else:
    N1_into_semi_pro = N1

# 零件2
if (comb[1] == 1):
    N2_into_semi_pro = (1 - data['p2']) * N2
else:
    N2_into_semi_pro = N2

# 零件3
if (comb[2] == 1):
    N3_into_semi_pro = (1 - data['p3']) * N3
else:
    N3_into_semi_pro = N3

# 零件4
if (comb[3] == 1):
    N4_into_semi_pro = (1 - data['p4']) * N4
else:
    N4_into_semi_pro = N4

# 零件5
if (comb[4] == 1):
    N5_into_semi_pro = (1 - data['p5']) * N5
else:
    N5_into_semi_pro = N5

# 零件6
if (comb[5] == 1):
    N6_into_semi_pro = (1 - data['p6']) * N6
else:
    N6_into_semi_pro = N6

# 零件7
if (comb[6] == 1):
    N7_into_semi_pro = (1 - data['p7']) * N7
else:
    N7_into_semi_pro = N7

# 零件8
if (comb[7] == 1):
    N8_into_semi_pro = (1 - data['p8']) * N8
else:
    N8_into_semi_pro = N8

# 求零件1-8的购买价格和检测成本之和
C_buy_and_text_parts = N1_into_semi_pro * data['e1'] + N2_into_semi_pro * data['e2'] + N3_into_semi_pro * data[
        'e3'] + N4_into_semi_pro * data['e4']
C_buy_and_text_parts = C_buy_and_text_parts + N5_into_semi_pro * data['e5'] + N6_into_semi_pro * data[
        'e6'] + N7_into_semi_pro * data['e7']
C_buy_and_text_parts = C_buy_and_text_parts + N8_into_semi_pro * data['e8'] + comb[0] * N1_into_semi_pro * data[
        't1'] + comb[1] * N2_into_semi_pro * data['t2']
C_buy_and_text_parts = C_buy_and_text_parts + comb[2] * N3_into_semi_pro * data['t3'] + comb[3] * N4_into_semi_pro * \
                           data['t4'] + comb[4] * N5_into_semi_pro * data['t5']
C_buy_and_text_parts = C_buy_and_text_parts + comb[5] * N6_into_semi_pro * data['t6'] + comb[6] * N7_into_semi_pro * \
                           data['t7'] + comb[7] * N8_into_semi_pro * data['t8']

# 求装配出来的半成品1-3
N1_finish_install = min(N1_into_semi_pro, N2_into_semi_pro, N3_into_semi_pro)
N2_finish_install = min(N4_into_semi_pro, N5_into_semi_pro, N6_into_semi_pro)
N3_finish_install = min(N7_into_semi_pro, N8_into_semi_pro)

# 半成品1-3装配费用
C_semi_pro_total_install = N1_finish_install * data['d1'] + N2_finish_install * data['d2'] + N3_finish_install * \
                               data['d3']
C_semi_pro_total_text = N1_finish_install * data['t9'] * comb[8] + N2_finish_install * data['t10'] * comb[
        9] + N3_finish_install * data['t11'] * comb[10]

# 半成品1-3各自的总废品率
# 半成品1总废品率
if (comb[0] + comb[1] + comb[2] == 3):  # 都检测
    p1_semi_pro_bad = 0.1
if (comb[0] + comb[1] + comb[2] == 1):  # 只检测其中一个
    p1_semi_pro_bad = 0.271
if (comb[0] + comb[1] + comb[2] == 2):  # 检测其中两个
    p1_semi_pro_bad = 0.19
if (comb[0] + comb[1] + comb[2] == 0):  # 都不检测
    p1_semi_pro_bad = 0.3439

# 半成品2总废品率
if comb[3] + comb[4] + comb[5] == 3:  # 都检测
    p2_semi_pro_bad = 0.1
if comb[3] + comb[4] + comb[5] == 1:  # 只检测其中一个
    p2_semi_pro_bad = 0.271
if comb[3] + comb[4] + comb[5] == 2:  # 检测其中两个
    p2_semi_pro_bad = 0.19
if comb[3] + comb[4] + comb[5] == 0:  # 都不检测
    p2_semi_pro_bad = 0.3439

# 半成品3总废品率
if comb[6] + comb[7] == 1:  # 只检测其中一个
    p3_semi_pro_bad = 0.19
if comb[6] + comb[7] == 2:  # 检测其中两个
    p3_semi_pro_bad = 0.1
if comb[6] + comb[7] == 0:  # 都不检测
    p3_semi_pro_bad = 0.271

# 半成品1-3中次品总的拆解费用
C_semi_pro_total_disconnect = comb[11] * p1_semi_pro_bad * N1_finish_install * data['h1'] + comb[
        12] * p2_semi_pro_bad * N2_finish_install * data['h2'] + comb[13] * p3_semi_pro_bad * N3_finish_install * data[
                                      'h3']

# 半成品1-3进入组装成品分别的个数
# 半成品1
if (comb[8] == 1):
    N1_into_pro = (1 - p1_semi_pro_bad) * N1_finish_install
else:
    N1_into_pro = N1_finish_install

# 半成品2
if (comb[9] == 1):
    N2_into_pro = (1 - p2_semi_pro_bad) * N2_finish_install
else:
    N2_into_pro = N2_finish_install

# 半成品3
if (comb[10] == 1):
    N3_into_pro = (1 - p3_semi_pro_bad) * N3_finish_install
else:
    N3_into_pro = N3_finish_install

# 组装出来的成品总数
N_pro_total = min(N1_into_pro, N2_into_pro, N3_into_pro)

# 成品中的总次品率
if (comb[8] + comb[9] + comb[10] == 3):  # 对半成品1-3都检验
    p_pro_bad = 0.1

if (comb[8] + comb[9] + comb[10] == 1):  # 只检测1个
    if (comb[8] == 1):
        p_pro_bad = (1 - p2_semi_pro_bad) * (1 - p3_semi_pro_bad) * 0.1 + p2_semi_pro_bad * (
                    1 - p3_semi_pro_bad) + (
                                1 - p2_semi_pro_bad) * p3_semi_pro_bad + p2_semi_pro_bad * p3_semi_pro_bad
    if (comb[9] == 1):
        p_pro_bad = (1 - p1_semi_pro_bad) * (1 - p3_semi_pro_bad) * 0.1 + p1_semi_pro_bad * (
                    1 - p3_semi_pro_bad) + (
                                1 - p1_semi_pro_bad) * p3_semi_pro_bad + p1_semi_pro_bad * p3_semi_pro_bad
    if (comb[10] == 1):
        p_pro_bad = (1 - p1_semi_pro_bad) * (1 - p2_semi_pro_bad) * 0.1 + p1_semi_pro_bad * (
                    1 - p2_semi_pro_bad) + (
                                1 - p1_semi_pro_bad) * p2_semi_pro_bad + p1_semi_pro_bad * p2_semi_pro_bad

if (comb[8] + comb[9] + comb[10] == 2):  # 检测两个
    if (comb[8] + comb[9] == 2):
        p_pro_bad = (1 - p3_semi_pro_bad) * 0.1 + p3_semi_pro_bad
    if (comb[8] + comb[10] == 2):
        p_pro_bad = (1 - p2_semi_pro_bad) * 0.1 + p2_semi_pro_bad
    if (comb[9] + comb[10] == 2):
        p_pro_bad = (1 - p1_semi_pro_bad) * 0.1 + p1_semi_pro_bad

if (comb[8] + comb[9] + comb[10] == 0):  # 全都不检测
    p_pro_bad = (1 - p1_semi_pro_bad) * (1 - p2_semi_pro_bad) * (1 - p3_semi_pro_bad) * 0.1 + p1_semi_pro_bad * (
                1 - p2_semi_pro_bad) * (1 - p3_semi_pro_bad) + (1 - p1_semi_pro_bad) * p2_semi_pro_bad * (
                            1 - p3_semi_pro_bad) + (1 - p1_semi_pro_bad) * (
                            1 - p2_semi_pro_bad) * p3_semi_pro_bad + p1_semi_pro_bad * p2_semi_pro_bad * p3_semi_pro_bad

# 成品中次品的数量
N_bad_in_pro = N_pro_total * p_pro_bad

# 生产成品的装配成本和检测成本之和
C_install_pro_total = N_pro_total * data['d4'] + comb[14] * N_pro_total * data['t12']

C_exchange = (1 - comb[14]) * N_bad_in_pro * data['d5']
C_disconnect_pro = comb[15] * N_bad_in_pro * data['h4']
C_exchange_new_pro = (1 - comb[14]) * N_bad_in_pro * data['r2']
# 成品中的次品所带来的成本
C_pro_bad_total = C_exchange + C_disconnect_pro + C_exchange_new_pro  # 调换损失+拆解费用+调换新产品的费用

# 成品的销售额
R_pro_sell = N_pro_total * data['r2']

# 半成品拆解出来的收益
# 设半成品1，2中零件1-6为次品的概率为5.5%
# 设在半成品3中，零件7，8为的概率为3.3%
R_semi_disconnect = comb[11] * (
            (1 - 0.05) * p1_semi_pro_bad * N1_finish_install * (data['e1'] + data['e2'] + data['e3'])) + comb[
                            12] * ((1 - 0.05) * p2_semi_pro_bad * N2_finish_install * (
            data['e4'] + data['e5'] + data['e6'])) + comb[13] * (
                                (1 - 0.03) % p3_semi_pro_bad * N3_finish_install * (data['e7'] + data['e8']))

# 由于半成品的成本较难直接计算，我们假设半成品的成本为零件成本+组装成本+零件检测成本的80%
e_semi_1 = (data['e1'] + data['e2'] + data['e3'] + data['t1'] * comb[0] + data['t2'] * comb[1] + data['t3'] * comb[
        2] + data['d1']) * 0.8
e_semi_2 = (data['e4'] + data['e5'] + data['e6'] + data['t4'] * comb[3] + data['t5'] * comb[4] + data['t6'] * comb[
        5] + data['d2']) * 0.8
e_semi_3 = (data['e7'] + data['e8'] + data['t7'] * comb[6] + data['t8'] * comb[7] + data['d3']) * 0.8

# 假设，在成品的废品中，半成品1，2为次品的概率为25%
# 假设，在成品的废品中，半成品3为次品的概率为15%
R_pro_disconnect = comb[15] * (
            N_bad_in_pro * (1 - 0.25) * e_semi_1 + N_bad_in_pro * (1 - 0.25) * e_semi_2 + N_bad_in_pro * (
            1 - 0.15) * e_semi_3)

L_total = R_pro_sell + R_semi_disconnect + R_pro_disconnect - C_buy_and_text_parts - C_semi_pro_total_install - C_semi_pro_total_text - C_semi_pro_total_disconnect - C_pro_bad_total
L_total_set.append(L_total)

# 找到最大值
max_value = max(L_total_set)

# 找到最大值的下标
max_index = L_total_set.index(max_value)
print(L_total_set[max_index])
print(valid_combinations[max_index])

print("最大值的下标是:", max_index)
