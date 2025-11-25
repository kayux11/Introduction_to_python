#Practical exercise 1
age = int(input("Enter your age: "))
if age >= 18 :
    print("You are eligible to vote.")
else :
    print("You are not eligible to vote yet.")

# practical exercise 2
#Discount calculator with ELIF
purchase_amount = float(input("Enter yur purchase amount: "))
if purchase_amount >= 1000: 
    discount = 0.1  # 10% discount
elif purchase_amount >= 500 :
    discount = 0.05 # 5% discount
else:
    discount = 0  # No discount
final_price = purchase_amount * (1-discount)
print(f"Final price after discount: ${final_price}",)

# Letter grade assigner with nested if statement
score = int(input("Enter your score: "),)
if score >=90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 50:
    grade = "D"
elif score >= 40:
    grade = "E"
else:
    grade = "F"
print("Your grade is; ",grade)

# The use of match case to simplifies checking for specific value
day = input("Enter a day of the week(monday - sunday): ",) .lower()
match day:
    case "monday":
        print("Ugh, Monday ...")
    case "tuesday":
        print("Just another working ...")
    case "wednesday":
        print("Hump day!")
    case "thursday":
        print("Almost there ...")
    case "friday":
        print("TGIF!")
    case "saturday" | "sunday":
        print("Weekend vibes!")
    case _:
        print("Invalid day entered.")

# Matching data type
value = input("Enter a value (number or string): ",)
match value:
    case int():
        print("You enter an integer:", value)
    case str():
        print("You enter a string:", value)
    case _:
        print("Invalid data type entered.")

# Matching age
age = int(input("Enter your age: "))
match age:
    case 18|19:
        if age >=18:
            print("You are eligble to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("Youare not yet eligible to vote.") 