sandwich_orders=['鸡肉','牛肉','猪肉','五香烟熏牛肉','五香烟熏牛肉','五香烟熏牛肉','番茄','五香烟熏牛肉']
print("五香烟熏牛肉已经卖完了")
while'五香烟熏牛肉' in sandwich_orders:
    sandwich_orders.remove('五香烟熏牛肉')
print(sandwich_orders)