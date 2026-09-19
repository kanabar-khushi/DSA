#4. Conditions

#1. Check whether a number is positive, negative, or zero.
print("--- This is the output for Question 1 positive, negative, or zero---")
num = float(input("Enter a number: "))

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2. Check whether a person is eligible to vote.
print("\n--- This is the output for Question 2 eligible to vote---")
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#3. Find the largest of three numbers.
print("\n--- This is the output for Question 3 largest---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

#4. Check whether a year is a leap year.
print("\n--- This is the output for Question 4 leap year---")
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#5. Create a grade system based on marks.
print("\n--- This is the output for Question 5 grade system---")
marks = float(input("Enter marks: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
elif marks >= 50:
    print("Grade: E")
else:
    print("Grade: F")

#6. Check whether a number is divisible by 5 and 11.
print("\n--- This is the output for Question 6 divisible by 5 and 11---")
num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print("The number is divisible by both 5 and 11")
else:
    print("The number is not divisible by both 5 and 11")

#7. Create a simple calculator using if-elif-else.
print("\n--- This is the output for Question 7 simple calculator ---")
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    print("Result:", a + b)
elif operator == "-":
    print("Result:", a - b)
elif operator == "*":
    print("Result:", a * b)
elif operator == "/":
    if b != 0:
        print("Result:", a / b)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")






