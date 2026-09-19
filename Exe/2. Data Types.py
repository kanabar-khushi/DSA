#2. Data Types

# 1. Demonstrate int, float, str, bool, and complex
print("--- This is the output for Question 1 demonstrate int, float, str, bool, and complex ---")
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")
d = input("Enter True or False: ") == "True"
e = complex(input("Enter a complex number (e.g. 3+4j): "))

print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, type(e))



# 2. Accept two numbers and display their data types
print("\n--- This is the output for Question 2 accept two numbers and display data types ---")
a = input("Enter first number: ")
b = input("Enter second number: ")

print("First:", a, "Type:", type(a))
print("Second:", b, "Type:", type(b))

a = float(a)
b = float(b)

print("After conversion:")
print("First:", a, "Type:", type(a))
print("Second:", b, "Type:", type(b))



# 3. Convert a string number into an integer and float
print("\n--- This is the output for Question 3 convert string to integer and float ---")
num = input("Enter a number: ")

integer_num = int(num)
float_num = float(num)

print("Integer:", integer_num, type(integer_num))
print("Float:", float_num, type(float_num))


# 4. Find the length of a string
print("\n--- This is the output for Question 4 length of a string ---")
text = input("Enter a string: ")

print("String:", text)
print("Length:", len(text))



# 5. Create a list, tuple, set, and dictionary and display their types
print("\n--- This is the output for Question 5 create list, tuple, set, and dictionary ---")
# List
my_list = input("Enter list elements separated by space: ").split()

# Tuple
my_tuple = tuple(input("Enter tuple elements separated by space: ").split())

# Set
my_set = set(input("Enter set elements separated by space: ").split())

# Dictionary
key = input("Enter dictionary key: ")
value = input("Enter dictionary value: ")
my_dict = {key: value}

print("\nList:", my_list, type(my_list))
print("Tuple:", my_tuple, type(my_tuple))
print("Set:", my_set, type(my_set))
print("Dictionary:", my_dict, type(my_dict))




