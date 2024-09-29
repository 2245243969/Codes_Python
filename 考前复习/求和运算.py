tn=0
list=[]
a=int(input('a= '))
b=int(input('b= '))
for i in range(b):
    tn=tn+a
    a*=10
    list.append(tn)
    print(tn)
print(f"前{b}个数的总数合为：{sum(list)}")