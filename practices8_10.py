def show_messages(messages,completed_messages):
    while messages:
        current_message = messages.pop()
        print(current_message)
        completed_messages.append(current_message)

def send_messages(completed_messages):
    for message in completed_messages:
        print(message)


messages=['数据结构','你怎么这么难懂','怎么这么难学啊！！！！','我不理解！！！！！！！！！',]
completed_messages=[]
show_messages(messages,completed_messages)
send_messages(completed_messages)
