x=int(input('x= '))
y=int(input('y= '))

if x>y:
    x,y=y,x

for factor in range(x,0,-1):
    if x%factor==0 and y%factor==0:
        print(f"{x}和{y}的最大公约数为：{factor}")
        print(f"{x}和{y}的最大公倍数为：{x*y//factor}")
        break
