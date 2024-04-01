class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"这家餐厅的名字是:{self.name} ，菜品的类型是:{self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅正在营业。")

class IceCreamStand(Restaurant):

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=['草莓味','芒果味','西瓜味','香草味',]

    def print_flavors(self):
        print(self.flavors)

the_icecreamstand=IceCreamStand('哈根达斯','雪糕')
the_icecreamstand.describe_restaurant()
the_icecreamstand.print_flavors()

