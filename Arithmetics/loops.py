# Iterating over list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Iterating over tuple: they are like list but immutable (unchangeable)
colors = ("red", "green", "blue", "yellow", "black", "pink", "brown", "white")
for color in colors:
    print(color)

# Looping through characters in string:
message = "Hello, World!"
for character in message:
    print(character)

# Iterating over ranges:
for number in range (0, 10):
    print(number)

#  WHILE LOOPS AND NESTED LOOPS
# Using input validation
age =0
while age < 18:
    age = int(input("Enter your age: "))
    print("you are older enough to proceed.")

# Guessi Game
secrete_number = 7
guess_count = 0
guess = 0
while guess != secrete_number:
    guess_count +=1
    guess = int(input("Guess a number between 1 and 10.: "))
    print(f"You guess it in {guess_count} tries!")


count = 0
while count < 10:
    print(f"Count is: {count}")
    count += 2  # Increment count to eventually make the condition False
print("Loop finished.")