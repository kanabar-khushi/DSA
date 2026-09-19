#5. Loops

#1. Print numbers from 1 to 10 using a for loop.
print("--- This is the output for Question 1 for loop---")
for i in range(1, 11):
    print(i)

#2. Print numbers from 10 to 1 using a while loop.
print("\n--- This is the output for Question 2 while loop---")
i = 10
while i >= 1:
    print(i)
    i -= 1
    
#3. Print the multiplication table of a number.
num = 5  # Change this to any number
print(f"\n--- This is the output for Question 3 (Table of {num}) ---")


for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#4. Find the sum of numbers from 1 to n.
n = 1  # Change this to your desired limit
print(f"\n--- This is the output for Question 4 (Sum up to {n}) ---")

total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"The sum is: {total_sum}")

#5. Find the factorial of a number.
num = 5  # Change this to calculate a different factorial
print(f"\n--- This is the output for Question 5 (Factorial of {num}) ---")

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print(f"The factorial of {num} is {factorial}")

#6. Print all even numbers between 1 and 100.
print("\n--- This is the output for Question 6 even numbers between 1 and 100---")
for i in range(2, 101, 2):
    print(i)
    
#7. Reverse a number using a loop.
num = 12345
print(f"\n--- This is the output for Question 7 (Reverse {num}) ---")  # Changed original_num to num

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = (reversed_num * 10) + digit
    num //= 10

print(f"Reversed number: {reversed_num}")

#8. Count the digits of a number.

num = 98765
print(f"\n--- This is the output for Question 8 (Counting digits of {num}) ---")  # Changed to num

count = 0
while num > 0:
    count += 1
    num //= 10

print(f"Number of digits: {count}")


#9. Check whether a number is prime.
num = 29  # Change to check a different number
print(f"\n--- This is the output for Question 9 (Checking prime for {num}) ---")

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

#10. Print Fibonacci series up to n terms.
print(f"\n--- This is the output for Question 10 (Fibonacci up to {n} terms) ---")
n = 10  # Number of terms to print
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b










