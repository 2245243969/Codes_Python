str1="k:1|k1:2|k2:3|k3:4"
def str2dict(str1):
    dict1={}
    for iterms in str1.split('|'):
        key,value = iterms.split(':')
        dict1[key]=int(value)
    return dict1
print(str2dict(str1))
str_list=str1.split('|')
print(str_list)