class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"这家餐厅的名字是:{self.name} ，菜品的类型是:{self.cuisine_type}")

    def open_restaurant(self):
        print("餐厅正在营业。")


the_restaurant=Restaurant('点都德','粤菜')
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()



