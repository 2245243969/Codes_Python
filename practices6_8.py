favorite_places={
    'meself': ['DaLian','GuangZhou','SuZhou','ChengDu'],
    'Xinyu Ma': ['NanJin','KunMing',],
    'Shuning Qian': ['ShanWei','ShenZheng','XiangGang'],
    'Huijun Chen': ['BeiJin','GuangZhou'],
    }
for name,places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")
