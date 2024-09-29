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

# 计算样本量
def calculate_min_sample_size(z_a, p0, delta):
    return math.ceil((z_a**2 * p0 * (1 - p0)) / delta**2)

# 计算所需样本量
n_95 = calculate_min_sample_size(z_95, p0, delta)
n_90 = calculate_min_sample_size(z_90, p0, delta)

print(f"在95%的信度下，所需的最小样本量为: {n_95}")
print(f"在90%的信度下，所需的最小样本量为: {n_90}")
