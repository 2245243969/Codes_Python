data=eval(input("请输入一个包含若干实属的列表："))
print(max(data,key=abs))