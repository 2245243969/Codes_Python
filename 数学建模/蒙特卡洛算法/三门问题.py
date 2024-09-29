import numpy as np

# np.random.randint(low,high,size)函数可在指定区间(low，high)内随机取出指定大小的整数
print(np.random.randint(1, 6, (5, 8)))  # 在区间[1，5]内随机取出木小为5*8的整数矩阵
print(np.random.randint(1, 6))  # 在区间[1，5]内随机取出1个整数

# (2)代码部分(在成功的条件下的概率)
n = 100000  # n代表蒙特卡罗模拟重复次数
a = 0  # a表示不改变主意时能赢得汽车的次数
b = 0  # b表示改变主意时能赢得汽车的次数
for i in range(n):  # 开始模拟n次
    x = np.random.randint(1, 4)  # 随机生成一个1-3之间的整数x表示汽车出现在第x扇门后
    y = np.random.randint(1, 4)  # 随机生成一个1-3之间的整数y表示自己选的门
    # 下面分为两种情况讨论:x=y和x!=y
    if x == y:  # 如果x和y相同，那么我们只有不改变主意时才能赢
        a += 1
    else:  # x!= y，如果x和y不同，那么我们只有改变主意时才能赢
        b += 1

print('蒙特卡洛方法得到的不改变主意时的获奖概率为：', a / n)
print('蒙特卡洛方法得到的改变主意时的获奖概率为：', b / n)

# 考虑失败情况的代码(无条件概率)
n = 100000  # n代表蒙特卡罗模拟重复次数
a = 0  # a表示不改变主意时能赢得汽车的次数
b = 0  # b表示改变主意时能赢得汽车的次数
c = 0  # c表示没有获奖的次数
for i in range(n):  # 开始模拟n次
    x = np.random.randint(1, 4)  # 随机生成一个1-3之间的整数x表示汽车出现在第x扇门后
    y = np.random.randint(1, 4)  # 随机生成一个1-3之间的整数y表示自己选的门
    change = np.random.randint(0, 2)  # change =0 不改变主意，change = 1 改变主意
    # 下面分为两种情况讨论:x=y和x!=y
    if x == y:  # 如果x和y相同，那么我们只有不改变主意时才能赢
        if change == 0:  # 不改变主意
            a += 1
        else:  # 改变了主意
            c += 1
    else:  # x=y,如果x和y不同，那么我们只有改变主意时才能赢
        if change == 0:  # 不改变主意
            c += 1
        else:  # 改变了主意
            b += 1

print('蒙特卡洛方法得到的不改变主意时的获奖概率为：', a / n)
print('蒙特卡洛方法得到的改变主意时的获奖概率为：', b / n)
print('蒙特卡洛方法得到的没有获奖的获奖概率为：', c / n)
