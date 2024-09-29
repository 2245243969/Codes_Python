import itertools

# 定义变量的值范围
x_values = [0, 1]

# 生成x1, x2, x3, x4的所有组合
all_combinations = list(itertools.product(x_values, repeat=4))

# 输出所有组合
for i, comb in enumerate(all_combinations, 1):
    print(f'Combination {i}: {comb}')

