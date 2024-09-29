x=input("请输入一个小于1000的整数：")
x=eval(x)
t=x
j=2
result=[]
while True:
    if t==1:
        break
    if t%j==0:
        result.append(j)
        t=t/j
    else:
        j+=1

print(x,"=","*".join(map(str,result)))