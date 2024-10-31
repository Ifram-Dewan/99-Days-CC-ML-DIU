# Variables and Data Types
name = "Ifram"
age = 20
height = 6
is_student = True

# Lists
Interest = ["Machine Learning", "Research", "Competitive programming"]
print(Interest[0])  # Accessing elements
Interest.append("DL")  # Adding an element
print(Interest)

# Dictionaries
person = {"name": "Ifram", "age": 20, "city": "Dhaka"}
print(person["name"])
person["age"] = 21  # Updating a value
print(person)

# Loops
for Interest in Interest:
    print(Interest)

# Functions
def greet(name):
    return f"Hello, {name}!"

print(greet("Ifram"))
