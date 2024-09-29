n=int(input("输入一个数字"))
s=0.0
if n%2==0:
    for i in range(2,n+1,2):
        s+=1.0/i
else:
    for i in range(1,n+1,2):
        s+=1.0/i
print(s)