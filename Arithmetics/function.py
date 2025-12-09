# Basic function
def greet():
    print("Assalamualaikum Waramatullahi Wabarakatu")
greet()

# Function With Parameters
def greet(name):
    print(f"Hello! {name}")
greet("joy")
greet("sharafudeen")
greet("muslim")
greet("Abdullah")

# Function That Returns a Value
def add(a, b):
    return a + b
result = add(4, 9)
print(result)


def add(a, b):
    return a + b
result = add(5, 3)
print(result)


# Function With Default Parameter
def greet(name = "friends"):
    print(f"Hello! {name}")
greet()
greet("abu")
greet("Zainab")


# Local Variable
# def my_func():
#     x = 10
#     print(x)

# my_func()
# print(x)  # ❌ Error: x doesn't exist outside

# Global Variable
# x = 20

# def show():
#     print(x)

# show()   # Output: 20

# Function With Multiple Returns
# num = int(input("Enter a number: "))
# def analyze(num):
#     if num % == 0:
#         return "Even"
#     else:
#         return "Odd"
# analyze(num)

# def analyze(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# analyze(5)
# def analyze(num):
#     if num % 2 == 0:
#         print("Even")
#     else:
#         print("Odd")

# analyze(num)

#Function With Unlimited Arguments (*args, **kwargs)
# *args = unlimited positional arguments
def total(*numbers):
    return sum(numbers)
print(total(4,6,7,8,))

# **kwargs = unlimited keyword arguments

def show_details(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

show_details(name="Ali", age=25, city="Lagos")


# Lambda functions
add = lambda x, y : x + y 
result = add(7, 8)
print(result)