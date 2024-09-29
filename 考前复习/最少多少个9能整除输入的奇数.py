zi=int(input("输入一个奇数："))
c9=1
m9=9
sum=9
while True:
    if sum % zi==0:
        break
    else:
        m9*=10
        sum+=m9
        c9+=1
print(f"{c9}个9可以被{zi}整除：{sum}")
print(sum/zi)