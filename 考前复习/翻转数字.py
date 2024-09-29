num1=input("请输入一个数字：")
num3=int(num1)
if num3>0:
    len_num=len(num1)
else:
    len_num=len(num1)-1

if num3<0:
    num2=-num3
else:
    num2=num3
print(f"num2={num2}")
sum=0
num1_reversed=num1[::-1]
for i in num1_reversed:
    if i!='-':
        sum+=int(i)
if sum%2==0:
    print(num3)
else:
    if num3>0:
        print(num1_reversed)
    else:
        print('-'+num1_reversed[:-1])