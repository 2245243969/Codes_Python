data=eval(input("请输入一个包含若干自然数的列表："))
temp=[]
for i in data:
    temp.append(len(str(i)))
print(temp)