str1=("东:1,北:2,财:3,经:4,大:5,学:6")
def s2d(s):
    dict_1={}
    for items in str1.split(","):
        key,value=items.split(":")
        dict_1[key]=value
    return dict_1
print(s2d(str1))