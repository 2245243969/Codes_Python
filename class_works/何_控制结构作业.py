m = '666'
s = 1

Num = input("请输入：")
if Num == m:
    print("登录成功")
elif Num != m:
    while s <= 2:
        print("密码错误，还有{}次机会".format(3 - s))
        Num = input("请再次输入")
        s = s + 1

    if s == 3:
        print("输入密码达到三次，请稍后登录")
