a=input("请输入一个数字：")
b=input("请输入一个数字：")

try:
    c=int(a)+int(b)
except ValueError:
    print("你应该输入数字而不是输入鸡对鸭说的玩意！！！！！")
else:
    print(int(a)+int(b))