# card = str(input("Enter product of your choice from the list(MTN, AIRTEL, GLO, 9MOBILE): ",)).lower
# qnty = float(input("Enter quantity of your choce: ",))
# mtn = 98.0
# if card == "mtn":
#     price1 = mtn * qnty
# print(f"Unit price for MTN is {price1}")

# count = 0
# while count <= 6 :
#     print(f"count is {count}")
#     count +=1
# print("Loop finished!")

# A multiplication table
# for i in range(1, 11):
#     for j in range(1, 11):
#         product = i * j
#         print(f"{i} * {j} = {product}", end="\+" )
# print()
          

# num = int(input("Enter a number: "))

# i = 1
# while i <= 12:
#     print(f"{num} x {i} = {num * i}")
#     i += 1


def salute():
    print("assalamualaikum")
salute()

def sub(a,b):
    return a - b
result = sub(20, 6)
print(result)

def salute(name):
    print(f"Assalamulaikumya {name}")
salute("habibi")
salute("Ustaz")
salute("Talib")