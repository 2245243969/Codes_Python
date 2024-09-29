import math
from scipy.stats import norm
import matplotlib.pyplot as plt

# 定义参数
p0 = 0.10  # 标称次品率
delta = 0.03  # 容许的误差幅度

# 显著性水平和对应的Z值
alpha_95 = 0.05
alpha_90 = 0.10
z_95 = norm.ppf(1 - alpha_95)
z_90 = norm.ppf(1 - alpha_90)

# 计算样本量的函数
def calculate_sample_size(z_alpha, p0, delta):
    return math.ceil((z_alpha**2 * p0 * (1 - p0)) / delta**2)

# 计算所需样本量
n_95 = calculate_sample_size(z_95, p0, delta)
n_90 = calculate_sample_size(z_90, p0, delta)

print(f"在95%的信度下，所需的最小样本量为: {n_95}")
print(f"在90%的信度下，所需的最小样本量为: {n_90}")

# 生成图表：不同显著性水平下样本量的变化
def plot_sample_size():
    alphas = [0.01 * i for i in range(5, 21)]  # 从5%到20%的显著性水平
    sample_sizes = [calculate_sample_size(norm.ppf(1 - alpha), p0, delta) for alpha in alphas]

    plt.figure(figsize=(8, 6))
    plt.plot(alphas, sample_sizes, marker='o', linestyle='-', color='b')
    plt.title('Sample Size vs Significance Level', fontsize=14)
    plt.xlabel('Significance Level (Alpha)', fontsize=12)
    plt.ylabel('Sample Size', fontsize=12)
    plt.axvline(x=0.05, color='r', linestyle='--', label="95% Confidence Level")
    plt.axvline(x=0.10, color='g', linestyle='--', label="90% Confidence Level")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 生成图表：样本量与误差范围的关系
def plot_sample_size_vs_error():
    deltas = [0.01 * i for i in range(1, 21)]  # 从1%到20%的误差范围
    sample_sizes_95 = [calculate_sample_size(z_95, p0, delta) for delta in deltas]
    sample_sizes_90 = [calculate_sample_size(z_90, p0, delta) for delta in deltas]

    plt.figure(figsize=(8, 6))
    plt.plot(deltas, sample_sizes_95, label="95% Confidence Level", marker='o', linestyle='-', color='b')
    plt.plot(deltas, sample_sizes_90, label="90% Confidence Level", marker='o', linestyle='-', color='g')
    plt.title('Sample Size vs Error Margin', fontsize=14)
    plt.xlabel('Error Margin (Delta)', fontsize=12)
    plt.ylabel('Sample Size', fontsize=12)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 运行生成图表
plot_sample_size()
plot_sample_size_vs_error()
