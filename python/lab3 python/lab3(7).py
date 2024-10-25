# input amount from user

amount = int(input("Enter amount : "))  # 17600

if amount % 100 == 0:
    if amount >= 2000:
        notes = amount // 2000  # 17600/2000= 8
        print(f"2000 X {notes} = {notes * 2000}")  # 2000 X 8 = 16000
        amount = amount - (notes * 2000)  # amount = 17600 - 16000= 1600

    if amount >= 500:
        notes = amount // 500  # 1600/500= 3
        print(f"500 X {notes} = {notes * 500}")  # 500 X 3 = 1500
        amount = amount - (notes * 500)  # amount = 1600 - 1500= 100

    if amount >= 200:
        notes = amount // 200
        print(f"200 X {notes} = {notes * 200}")
        amount = amount - (notes * 200)

    if amount >= 100:
        notes = amount // 100  # 100/100= 1
        print(f"100 X {notes} = {notes * 100}")  # 100 X 1 = 100
        amount = amount - (notes * 100)  # amount = 100 - 100= 0
else:
    print("Amount should be multiple of 100!!")