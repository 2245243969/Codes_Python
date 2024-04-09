sandwich_orders=['鸡肉三明治','牛肉三明治','番茄三明治']
finished_sandwiches=[]

while sandwich_orders:
    finished_order=sandwich_orders.pop(0)
    print(f"制作好了您的{finished_order}")
    finished_sandwiches.append(finished_order)

print(f"您已经制作了{finished_sandwiches[0]},{finished_sandwiches[1]}和{finished_sandwiches[2]}")