#6.Functions

#1.Write a function to print "Hello, World!".
print("--- This is the output for Question 1 Hello, World!---")
def hello():
    print("Hello, World!")
hello()

#2.Write a function that takes a name and prints a greeting.
print("--- This is the output for Question 2 Greeting---")
def greet(name):
    print("Hello,", name)
name = input("Enter your name: ")
greet(name)

#3.Write a function to add two numbers.
print("--- This is the output for Question 3 Add Two Number---")
def add(a, b):
    return a + b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a, b)
print("Addition =", result)

#4.Write a function to find the square of a number
print("--- This is the output for Question 4: Square of a Number ---")
def square(number):
    return number * number
number = int(input("Enter a number: "))
result = square(number)
print("Square =", result)

#5.Write a function to check whether a number is even or odd.
print("--- This is the output for Question 5: Even or Odd---")
def check_even_odd(number):
    if number % 2 == 0:
        print("The number is Even.")
    else:
        print("The number is Odd.")
number = int(input("Enter a number: "))
check_even_odd(number)

#6.Write a function to find the maximum of two numbers.
print("--- This is the output for Question 6: Maximum of Two Numbers ---")
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = find_max(a, b)
print("Maximum number =", result)

#7.Write a function to convert Celsius to Fahrenheit.
print("---This is the output for Question 7: Celsius to Fahrenheit ----")
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print("Temperature in Fahrenheit =", fahrenheit)

#8.Write a function to calculate the area of a circle.
print("---This is the output for Question 8: Area of A Circle---")
def circle_area(radius):
    return 3.14 * radius * radius
radius = float(input("Enter radius of the circle: "))
area = circle_area(radius)
print("Area of the circle =", area)

#9.Write a function to calculate the factorial of a number.
print("--- This is the output for Question 9: Factorial of a Number ---")
def factorial(number):
    if number < 0:
        return None

    result = 1
    for i in range(1, number + 1):
        result = result * i
    return result

number = int(input("Enter a number: "))
result = factorial(number)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial =", result)

#10.Write a function to check whether a number is positive, negative, or zero.
print("--- This is the output for Question 10: Positive, Negative, or Zero ---")
def check_number(number):
    if number > 0:
        print("The number is Positive.")
    elif number < 0:
        print("The number is Negative.")
    else:
        print("The number is Zero.")
number = float(input("Enter a number: "))
check_number(number)

#11.Write a function to find the maximum of three numbers.
print("--- This is the output for Question 11: Maximum of Three Numbers ---")
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
maximum = find_max(a, b, c)
print("Maximum number =", maximum)

#12.Write a function to count vowels in a string.
print("--- This is the output for Question 12: Count Vowels in a String ---")
def count_vowels(text):
    count = 0
    for char in text:
        if char.lower() in "aeiou":
            count = count + 1
    return count
text = input("Enter a string: ")
result = count_vowels(text)
print("Number of vowels =", result)

#13.Write a function to reverse a string.
print("--- This is the output for Question 13: Reverse a String ---")
def reverse_string(text):
    return text[::-1]
text = input("Enter a string: ")
result = reverse_string(text)
print("Reversed string =", result)

#14.Write a function to check whether a string is a palindrome.
print("--- This is the output for Question 14: Check Palindrome ---")
def check_palindrome(text):
    if text == text[::-1]:
        return True
    else:
        return False

text = input("Enter a string: ")
result = check_palindrome(text)

if result:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")

#15.Write a function to find the sum of all elements in a list.
print("--- This is the output for Question 15: Sum of List Elements ---")
def list_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = list_sum(numbers)
print("Sum of all elements =", result)

#16.Write a function to find the largest element in a list.
print("--- This is the output for Question 16: Largest Element in a List ---")
def find_largest(numbers):
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

if numbers:
    result = find_largest(numbers)
    print("Largest element =", result)
else:
    print("Please enter at least one number.")

#17.Write a function to remove duplicate elements from a list.
print("--- This is the output for Question 17: Remove Duplicate Elements ---")
def remove_duplicates(numbers):
    unique = []
    for number in numbers:
        if number not in unique:
            unique.append(number)
    return unique

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = remove_duplicates(numbers)
print("List after removing duplicates =", result)

#18.Write a function to count how many times an element appears in a list.
print("--- This is the output for Question 18: Count Element Occurrences ---")
def count_element(numbers, element):
    count = 0
    for number in numbers:
        if number == element:
            count = count + 1
    return count

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
element = int(input("Enter the element to count: "))
result = count_element(numbers, element)
print("Element", element, "appears", result, "time(s).")

#19.Write a function to check whether a number is prime.
print("--- This is the output for Question 19: Check Prime Number ---")
def check_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

number = int(input("Enter a number: "))

if check_prime(number):
    print("The number is Prime.")
else:
    print("The number is not Prime.")

#20.Write a function to return all prime numbers between two numbers.
print("--- This is the output for Question 20: Prime Numbers Between Two Numbers ---")
def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def prime_numbers(start, end):
    primes = []

    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)

    return primes

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
result = prime_numbers(start, end)
print("Prime numbers =", result)

#21.Write a function to calculate Fibonacci numbers.
print("--- This is the output for Question 21: Fibonacci Numbers ---")
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter the number of terms: "))
print("Fibonacci series:")
fibonacci(n)

#22.Write a function to find the second-largest number in a list.
print("\n--- This is the output for Question 22: Second-Largest Number ---")
def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.sort()
    return unique_numbers[-2]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = second_largest(numbers)

if result is None:
    print("At least two different numbers are required.")
else:
    print("Second-largest number =", result)

#23.Write a function to sort a list without using sort().
print("--- This is the output for Question 23: Sort a List ---")
def sort_list(numbers):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]

    return numbers

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sort_list(numbers)
print("Sorted list =", result)

#24.Write a function to merge two lists and remove duplicates.
print("--- This is the output for Question 24: Merge Two Lists and Remove Duplicates ---")
def merge_lists(list1, list2):
    merged = list1 + list2
    unique = []

    for item in merged:
        if item not in unique:
            unique.append(item)

    return unique

list1 = list(map(int, input("Enter elements of first list: ").split()))
list2 = list(map(int, input("Enter elements of second list: ").split()))

result = merge_lists(list1, list2)
print("Merged list without duplicates =", result)
