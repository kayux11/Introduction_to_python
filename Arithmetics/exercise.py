number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
sum_result = number1 + number2
diff_result = number1 - number2
divid_result = number1 / number2
mult_result = number1 * number2
print(f"sum of {number1} and {number2} is {sum_result} ")
print(f"difference of {number1} and {number2} is {diff_result}")
print(f"qoutient of {number1} and {number2} is {divid_result}")
print(f"multiplication of {number1} and {number2} is {mult_result}")


# # BMI Calculation
weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))

print("Your BMI is", weight / (height ** 2))


# # ConvertbCelcius to Fahreheit
# celcius = float(input("Enter temperature in Celcius: ",))

# print("Equivalent Temperature in Fahreheit is", (celcius * 9/5) + 32 )

# # Average of Number
# num1 = float(input("Enter the first number: ",))
# num2 = float(input("Enter the second number: ",))
# num3 = float(input("Enter the third number: ",))
# sum = num1 + num2 + num3

# print(f"Average is", sum/3)


# # Area of a circle
r = 2
print("Area of a circle is", 3.142*(r**2))

# Simple interest
principal = 10000
rate = 5
time = 3

print("SI =", (principal * rate * time)/100)

# # Time converter
hrs = 130 //60 
min = 130 %60
print(hrs, min)

# Simple calculator
num1 = float(input("Enter first number: ",))
num2 = float(input("Enter second number: ",))
ops = input("Input operation(+, -, *, /): ",)
sum = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2

if ops == "+" :
    print(f"Addition of first number and second number is: {sum}",)
elif ops == "-" :
    print(f"Subtraction of second number from first number is: {sub}",)
elif ops == "*" :
    print(f"Multiplication of first and second number is: {mult}",)
elif ops =="/":
    if num2 !=0:
        print(f"Division of first number by second number is: {div}",)
    else:
        print("You can not divide by zero")
else:
    print("Invalid operation. Please choose from; +, -, *, /")