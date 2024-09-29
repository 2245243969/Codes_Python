# 矩阵位乘的分治写法代码实现

import numpy as np

def matrix_multiply_recursive(A, B):
    """递归地进行矩阵乘法的分治法实现"""



    # 获取矩阵的大小
    n = len(A)

    # 当矩阵只有 1x1 时，直接返回两个数的乘积
    if n == 1:
        return [A[0][0] * B[0][0]]

    # 将矩阵划分成 4 个子矩阵
    mid = n // 2

    # 分解矩阵 A 和 B
    A11 = A[:mid, :mid]  # 左上
    A12 = A[:mid, mid:]  # 右上
    A21 = A[mid:, :mid]  # 左下
    A22 = A[mid:, mid:]  # 右下

    B11 = B[:mid, :mid]  # 左上
    B12 = B[:mid, mid:]  # 右上
    B21 = B[mid:, :mid]  # 左下
    B22 = B[mid:, mid:]  # 右下

    # 递归计算子矩阵的乘积
    C11 = matrix_add(matrix_multiply_recursive(A11, B11),
                     matrix_multiply_recursive(A12, B21))
    C12 = matrix_add(matrix_multiply_recursive(A11, B12),
                     matrix_multiply_recursive(A12, B22))
    C21 = matrix_add(matrix_multiply_recursive(A21, B11),
                     matrix_multiply_recursive(A22, B21))
    C22 = matrix_add(matrix_multiply_recursive(A21, B12),
                     matrix_multiply_recursive(A22, B22))

    # 将结果拼接回一个完整的矩阵
    C = np.zeros((n, n))
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22

    return C

def matrix_add(A, B):
    """计算矩阵相加"""

    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__ == "__main__":
    # 定义两个矩阵
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])

    # 调用分治法矩阵乘法
    C = matrix_multiply_recursive(A, B)

    # 打印结果
    print("矩阵 A:")
    print(A)
    print("矩阵 B:")
    print(B)
    print("矩阵 A * B 的结果:")
    print(C)