import numpy as np
# 定义判断矩阵A
A = np.array([[1, 2, 3, 5], [1/2, 1, 1/2, 2], [1/3, 2,
1, 2], [1/5, 1/2, 1/2, 1]])
# 计算每列的和
ASum = np.sum(A, axis=0)
# 获取A的行和列
n, _ = A.shape
# 归一化
Stand_A = A / ASum
# 各列相加到同一行
ASumr = np.sum(Stand_A, axis=1)
# 计算权重向量
weights = ASumr / n
print(weights)