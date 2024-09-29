n=int(input("请输入一个自然数："))
a=[n]
while n!=1:
    if n%2==0:
        n=n/2
    else:
        n=3*n+1
    a.append(n)
print(len(a))
