a=eval(input("请输入一个包含若干整数的列表："))
b=eval(input("请再输入一个包含若干整数的列表："))
temp=0
for i in range(len(a)):
    temp+=a[i]*b[i]
print(temp)