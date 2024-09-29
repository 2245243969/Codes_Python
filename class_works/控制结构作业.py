original_code="123456"
num=0
while num!=3 :
    enter_code=input('请输入密码：')
    if original_code==enter_code :
        print("登录成功\n")
        exit()
    else :
        if num==2:
            print("输入密码达到三次，请稍后登录。")
            exit()
        else:
            print(f"密码错误，还有{2-num}次机会\n")
            num=num+1
