#1. Variables

#(1). Create variables to store name, age, and city and display them.
print("--- This is the output for Question 1 store name, age, and city ---")
Name=input("Enter name:")
Age=int(input("Enter age:"))
City=input("Enter city:")
print(Name)
print(Age)
print(City)

# (2). Swap the values of two variables.
print("\n--- This is the output for Question 2: Swap Variables ---")

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

print("\nBefore Swapping:")
print("a =", a)
print("b =", b)

# Swapping the values
a, b = b, a

print("\nAfter Swapping:")
print("a =", a)
print("b =", b)

#3. Calculate the area of a rectangle using variables.
print("\n--- This is the output for Question 3 area of a rectangle ---")
length=float(input("\nEnter the length of the rectangle: "))
width=float(input("Enter the width of the rectangle: "))

area=length*width

print(f"The area of the rectangle is: {area}")

#4. Calculate simple interest using variables.
print("\n--- This is the output for Question 4 simple interest ---")
principal = float(input("\nEnter the principal amount: "))
rate = float(input("Enter the rate : "))
year = float(input("Enter the year : "))

simple_interest = (principal * rate * year) / 100

print(f"----Result-----")
print(f"Principal: ${principal:,.2f}")
print(f"Rate: {rate:.2f}%")
print(f"Years: {year:.1f} years")
print(f"\nThe Simple Interest earned is: {simple_interest}")

#5. Convert Celsius temperature to Fahrenheit.
print("\n--- This is the output for Question 5 celsius to fahrenheit ---")
celsius = float(input("\nEnter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("celsius:",celsius)
print("fahrenheit:",fahrenheit)





