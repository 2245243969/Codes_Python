age = int(input("Please tell me your current age :"))
while True:
    if age<3:
        print("free")
        break
    if 3<=age<12:
        print("10元")
        break
    else:
        print("15元")
        break