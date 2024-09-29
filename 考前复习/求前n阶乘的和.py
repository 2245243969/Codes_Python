n=int(input("n= "))
s=0
t=1
for i in range(1,n+1):
    t*=i
    s+=t
print(f"前{n}阶乘的和为：{s}")