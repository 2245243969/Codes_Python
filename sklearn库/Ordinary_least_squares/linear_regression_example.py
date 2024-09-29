# Code source: Jaques Grobler
# License: BSD 3 clause

import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Load the diabetes dataset
# diabetes_x为该数据集的特征矩阵，diabetes_y为目标变量（即糖尿病进展的一个连续值），是模型要预测的结果
# return_x_y=True返回特征和目标变量为两个独立的数组
diabetes_X, diabetes_y = datasets.load_diabetes(return_X_y=True)

# Use only one feature
# np.newaxis用于将原来的二维数组转变为二维列向量
diabetes_X = diabetes_X[:, np.newaxis, 2]

# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]  # 包含除最后20个样本外的所有数据，作为训练集。
diabetes_X_test = diabetes_X[-20:]  # 最后20个样本，作为测试集。用来验证模型性能的未见过的数据。

# Split the targets into training/testing sets
diabetes_y_train = diabetes_y[:-20]  # 包含除最后 20 个样本外的所有目标变量，作为训练集的标签。
diabetes_y_test = diabetes_y[-20:]  # 最后 20 个样本的标签，作为测试集的实际值。

# Create linear regression object
regr = linear_model.LinearRegression()  # 创建线性回归模型对象。

# Train the model using the training sets
regr.fit(diabetes_X_train, diabetes_y_train)  # .fit()函数，用（）中的训练集来拟合线性回归模型，找到最佳的回归系数

# Make predictions using the testing set
diabetes_y_pred = regr.predict(diabetes_X_test)  # .predict()函数，使用训练好的模型对测试集数据进行预测

# The coefficients
print("Coefficients: \n", regr.coef_)  # .coef_用来返回模型的回归系数

# The mean squared error
# mean_squared_error()函数，用于计算模型预测值与真实值之间的均方误差。均方误差越小，模型的性能越好
print("Mean squared error: %.2f" % mean_squared_error(diabetes_y_test, diabetes_y_pred))

# The coefficient of determination: 1 is perfect prediction
# r2_score()函数，用于决定系数（R方）表示模型对数据的拟合优度，取值范围为0到1，值越接近1，模型拟合效果越好
print("Coefficient of determination: %.2f" % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test, color="black")
plt.plot(diabetes_X_test, diabetes_y_pred, color="blue", linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()
