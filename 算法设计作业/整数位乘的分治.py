# 整数位乘的分治写法代码实现

# Karatsuba乘法的分治实现
def karatsuba(x,y):
    """Karatsuba算法计算二进制数位乘"""

    # 如果x或者y小于2时，直接返回乘积
    if x < 2 or y < 2:
        return x * y

    # 计算二进制数字的长度
    max_length = max(x.bit_length(),y.bit_length())
    half = max_length // 2

    # 将x和y拆分成高位和低位部分,a为x的高位，b为x的低位,c为y的高位，d为y的低位
    a = x >> half
    b = x & ((1 << half) - 1)
    c = y >> half
    d = y & ((1 << half) - 1)

    # 递归计算Karatsuba公式中的量
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ab_cd = karatsuba(a+b,c+d)

    result = (ac << (2 * half)) + ((ab_cd - ac - bd) << half) + bd

    return result

# 测试
if __name__ == "__main__":
    # 二进制输入
    x = int('11010110', 2)
    y = int('1011001', 2)

    result = karatsuba(x, y)

    # 输出二进制结果
    print(f"{bin(x)} 和 {bin(y)} 的乘积是: {bin(result)}")
    # 输出十进制结果
    print(f"{x} 和 {y} 的乘积是: {result}")