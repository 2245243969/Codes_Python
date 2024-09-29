import itertools
import matplotlib.pyplot as plt

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=4))

valid_combinations = [comb for comb in all_combinations]

# 多组 data，每组数据都包括 p1, p2, p3 等参数
data_sets = [
    {'p1': 0.1, 'p2': 0.2, 'p3': 0.1, 'b1': 4, 'b2': 18, 'c1': 8, 'c2': 1, 'c3': 6, 'c4': 2, 'c5': 10, 'c6': 5,
     'r1': 56},
    {'p1': 0.15, 'p2': 0.25, 'p3': 0.05, 'b1': 5, 'b2': 20, 'c1': 9, 'c2': 1.5, 'c3': 6.5, 'c4': 2.2, 'c5': 11, 'c6': 6,
     'r1': 60},
    {'p1': 0.12, 'p2': 0.18, 'p3': 0.08, 'b1': 4.5, 'b2': 19, 'c1': 8.5, 'c2': 1.2, 'c3': 6.2, 'c4': 2.1, 'c5': 10.5,
     'c6': 5.5, 'r1': 58},
    {'p1': 0.09, 'p2': 0.22, 'p3': 0.1, 'b1': 3.8, 'b2': 17, 'c1': 7.5, 'c2': 1.1, 'c3': 5.8, 'c4': 1.9, 'c5': 9.5,
     'c6': 4.8, 'r1': 54},
    {'p1': 0.2, 'p2': 0.3, 'p3': 0.12, 'b1': 5.2, 'b2': 21, 'c1': 10, 'c2': 1.8, 'c3': 7, 'c4': 2.4, 'c5': 12,
     'c6': 6.2, 'r1': 62},
    {'p1': 0.05, 'p2': 0.1, 'p3': 0.05, 'b1': 3.5, 'b2': 16, 'c1': 7, 'c2': 1, 'c3': 5.5, 'c4': 1.8, 'c5': 9, 'c6': 4.5,
     'r1': 52}
]

# 将每一次生成的 L_total 存入 L_total_list 中
L_total_list = []

# N 值固定
N = 1000

# 遍历每组数据
for data in data_sets:
    # 输出当前数据组信息
    print(f"Processing data set: {data}")

    # 对每一组数据的所有组合进行运算
    for comb in valid_combinations:
        print(f"x1={comb[0]}, x2={comb[1]}, x3={comb[2]}, y1={comb[3]}")

        # 计算各项成本
        C1_buy = N / (1 - data['p1'] * (1 - comb[0]))
        C2_buy = N / (1 - data['p2'] * (1 - comb[1]))
        C1_text = comb[0] * N / (1 - data['p1']) * data['c1']
        C2_text = comb[1] * N / (1 - data['p2']) * data['c2']
        C_install = data['c3'] * N
        C_finish_text = comb[2] * data['p3'] * N

        # 计算合格率 p4
        p4 = (1 - data['p1'] * (1 - comb[0])) * (1 - data['p2'] * (1 - comb[1])) * (1 - data['p3'] * (1 - comb[2]))

        # 计算调换损失和拆解费用
        C_change_cost = (1 - p4) * N * data['c5']
        C_disconnection_cost = (1 - p4) * (
                    comb[3] * N * data['c6'] + N / (1 - data['p1']) * comb[0] * data['c1'] + N / (1 - data['p2']) *
                    comb[1] * data['c2']) + comb[2] * data['p3'] * N * (1 - p4)

        # 计算总收入
        R_total = (N * p4 * (1 - data['p3'])) * data['r1']

        # 计算总利润 L_total
        L_total = R_total - C1_buy - C2_buy - C1_text - C2_text - C_install - C_finish_text - C_change_cost - C_disconnection_cost

        # 如果 L_total 为正，将其存入 L_total_list
        if L_total >= 0:
            L_total_list.append(L_total)
            print(f"L_total: {L_total}")
        else:
            print("L_total: 0")
            L_total_list.append(0)

# 输出最终结果
print("All L_total values:")
print(L_total_list)
