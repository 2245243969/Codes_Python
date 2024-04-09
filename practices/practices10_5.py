from pathlib import Path
path = Path('guest_book.txt')
guest_list=[]
while True:
    guest_name=input("请输入用户的名字（输入退出以退出输入）：")
    if guest_name=='退出':
        break
    else:
        guest_list.append(guest_name)

guest_list.reverse()
guestlist=(guest_list.pop()+'\n')
for name in guest_list:
    guestlist+=(name+'\n')

path.write_text(guestlist)





