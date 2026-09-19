#3. Operators

# 1. Perform addition, subtraction, multiplication, and division.
print("--- This is the output for Question 1 addition, subtraction, multiplication, and division ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# 2. Find the remainder and quotient of two numbers.
print("\n--- This is the output for Question 2 remainder and quotient ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Quotient:", a // b)
print("Remainder:", a % b)

# 3. Check whether a number is even or odd.
print("\n--- This is the output for Question 3 even or odd ---")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")


# 4. Compare two numbers using relational operators.
print("\n--- This is the output for Question 4 relational operators ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# 5. Demonstrate logical operators (and, or, not).
print("\n--- This is the output for Question 5 logical operators ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b > 0:", a > 0 or b > 0)
print("not(a > 0):", not(a > 0))


# 6. Demonstrate assignment operators (+=, -=, *=, /=).

print("\n--- This is the output for Question 6 assignment operators ---")
a = float(input("Enter a number: "))

a += 5
print("After += 5:", a)

a -= 2
print("After -= 2:", a)

a *= 3
print("After *= 3:", a)

a /= 2
print("After /= 2:", a)



# 7. Find the largest of two numbers using comparison operators.
print("\n--- This is the output for Question 7 largest of two numbers ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest number:", a)
elif b > a:
    print("Largest number:", b)
else:
    print("Both numbers are equal")




