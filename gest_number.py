import random

random_number = random.randint(1, 100)
gust_name=input("请问该怎么称呼你呢？")
while True:
    print(f"{gust_name}你好！请输入你想要猜的次数来猜一个小于100的数(不要超过十四次哦)：")
    try:
        gest_number = int(input())

    except ValueError:
            print(f"{gust_name}你还没有输入数字哦，请再输入一次")
            gest_number=int(input())



    if gest_number>14:
        print(f"啊~~{gust_name}，次数太多了，我顶不住呢~~~")
        print("请再输入一次数字吧。")
        continue
    else:
        break
print("不过放心，我会提醒你大了还是小了")
print("准备好接受挑战了吗？")
num=eval(input("请输入一个数，并按下回车开始"))
count=1
while True:
    if num==random_number:
        print("恭喜你，你猜对了！！！！！")
        break
    else:
        if num<random_number:
            print("猜小了呢。")
            num=int(input("请输入一个数："))

        else:
            print("猜大了呢。")
            num=int(input("请输入一个数：" ))

    count=count+1
    if count==gest_number:
        print(f"这个{gust_name}就是菜啦，这都没猜对！\n其实正确的数是{random_number}")
        break