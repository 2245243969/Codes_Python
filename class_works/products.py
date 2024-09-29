# 超市货品统计系统
products = {}
def add_products(id, name, price, quantity):
    """添加商品信息"""
    # 先检测这个商品和id是否已经存在
    a, b = 1, 1
    for existing_id, (existing_name,_,_) in products.items():
        if existing_name == name:
            print(f"商品{name}，已经存在，不需要进行添加。")
            a = 0
        if existing_id == id:
            print(f"这个id:{id}已经存在。")
            b = 0
        if a == 0 or b == 0:
            return
    # 添加商品
    products[id] = (name, price, quantity)
    print("商品已经添加成功。")


def find_product_information(id):
    """查询商品基本信息"""
    if id in products:
        name, price, quantity = products[id]
        return f"这个id已找到，对应的商品名字为：{name}，价格为{price}元，进货数量为{quantity}件。"
    else:
        return "这个id下没有对应的商品。"


def delete_product(id):
    """删除商品信息"""
    if id in products:
        del products[id]
        return "商品删除成功。"
    else:
        return "商品不存在。"


def total_cost():
    """统计进货总额"""
    total_cost = 0
    for _, price, quantity in products.values():
        total_cost += price * quantity
    return total_cost

# 添加货品
add_products("001", "面包", 1, 100)
add_products("002", "牛奶", 2, 100)

# 查询货品
print(find_product_information("001"))
print(find_product_information("003"))

# 删除货品
print(delete_product("003"))

# 统计进货总额
print(f"目前的进货总额为: {total_cost():.1f}")