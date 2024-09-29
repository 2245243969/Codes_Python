import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split#将数据集划分为训练集和测试集，分别用于训练模型和评估模型性能。
from sklearn.linear_model import LinearRegression

# 固定随机种子以确保可重复性
np.random.seed(42)

# 生成数据
n_samples, n_features = 200, 50
X = np.random.randn(n_samples, n_features)  # 生成正态分布的自变量
true_coef = 3 * np.random.randn(n_features)  # 生成一个含有 50 个元素的随机系数向量，乘以 3 增加其幅度。
true_coef[true_coef < 0] = 0  # 将系数向量中所有负值置为 0，确保系数非负（用于非负最小二乘回归 NNLS）
y = np.dot(X, true_coef)  # 根据X和系数生成目标变量y

# 在目标变量 y 中加入随机噪声，以模拟真实数据中的随机波动
y += 5 * np.random.normal(size=(n_samples,))#生成一个与 y 大小相同的随机噪声向量，每个噪声值来自标准正态分布，乘以 5 使噪声较为明显

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# 使用正约束的线性回归（非负最小二乘，NNLS）
reg_nnls = LinearRegression(positive=True)
y_pred_nnls = reg_nnls.fit(X_train, y_train).predict(X_test)  # 训练模型并进行预测
r2_score_nnls = r2_score(y_test, y_pred_nnls)  # 计算R2分数
print("NNLS R2 score:", r2_score_nnls)

# 使用普通线性回归（OLS）
reg_ols = LinearRegression()
y_pred_ols = reg_ols.fit(X_train, y_train).predict(X_test)  # 训练模型并进行预测
r2_score_ols = r2_score(y_test, y_pred_ols)  # 计算R2分数
print("OLS R2 score:", r2_score_ols)

# 可视化两组回归系数的比较
fig, ax = plt.subplots()
ax.plot(reg_ols.coef_, reg_nnls.coef_, linewidth=0, marker=".", label='Coefficients')  # 散点图

# 添加对角线参考线
low_x, high_x = ax.get_xlim()  # 获取x轴范围
low_y, high_y = ax.get_ylim()  # 获取y轴范围
low = max(low_x, low_y)  # 确定对角线的低端
high = min(high_x, high_y)  # 确定对角线的高端
ax.plot([low, high], [low, high], ls="--", c=".3", alpha=0.5, label='y=x')  # 对角线

# 设置轴标签
ax.set_xlabel("OLS regression coefficients", fontweight="bold")
ax.set_ylabel("NNLS regression coefficients", fontweight="bold")

# 显示图例
ax.legend()

# 显示图像
plt.show()
