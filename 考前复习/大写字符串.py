string = input('请输入一个字符串：')
if not string.isupper():
    print('该字符串非全大写')
    string=string.upper()
else:
    print("该字符串全大写")
print(string)