# Python Program to perform operations on List, Tuple and Dictionary

# ---------------- LIST OPERATIONS ----------------
print("----- LIST OPERATIONS -----")

# Create a list
my_list = [10, 20, 30, 40, 50]
print("Original List:", my_list)

# Add a value
my_list.append(60)
print("After adding value:", my_list)

# Add a new value at a specific position
my_list.insert(2, 25)
print("After inserting value:", my_list)

# Remove a value
my_list.remove(30)
print("After removing value:", my_list)

# Find list size
print("List size:", len(my_list))

# Sort list in ascending order
my_list.sort()
print("Ascending order:", my_list)


# ---------------- TUPLE OPERATIONS ----------------
print("\n----- TUPLE OPERATIONS -----")

# Create a tuple
my_tuple = (10, 20, 30, 40, 50)
print("Tuple:", my_tuple)

# Access tuple value
print("First value:", my_tuple[0])

# Find tuple size
print("Tuple size:", len(my_tuple))

# Find a value in tuple
print("Number of 30:", my_tuple.count(30))


# ---------------- DICTIONARY OPERATIONS ----------------
print("\n----- DICTIONARY OPERATIONS -----")

# Create dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python"
}

print("Dictionary:", student)

# Display keys
print("Keys:", student.keys())

# Display values
print("Values:", student.values())

# Display key and value
for key, value in student.items():
    print(key, ":", value)

# Add a new key-value pair
student["city"] = "Ahmedabad"
print("After adding new key-value:", student)

# Remove a key-value pair
student.pop("age")
print("After removing age:", student)

# Dictionary size
print("Dictionary size:", len(student))
