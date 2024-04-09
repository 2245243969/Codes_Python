class User:
    def __init__(self,first_name,last_name,age,gender):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.gender=gender

    def describe_user(self):
        full_name=self.first_name+self.last_name
        print(f"{full_name}，{self.gender}，{self.age}岁。")

    def greet_user(self):
        print(f"下午好，{self.last_name}，是时候该去学习了！！！！")


user_info = User('周','健坤',19,'男')
user_info.describe_user()
user_info.greet_user()