def fib(n):
    a,b=1,1
    for i in range(n):
        if i%10==0:
            print("\n")
        print(a,end=" ")
        temp=a
        a=b
        b=temp+b

num=int(input("请输入需要打印斐波那契数列的数据个数："))
fib(num)