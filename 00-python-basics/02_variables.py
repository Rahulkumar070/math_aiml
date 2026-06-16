# 02_variables.py
# Lesson: variables and data types.
# Run it with:  python 00-python-basics/02_variables.py

# A VARIABLE is a name that points to a value.
# Python has a few basic TYPES of values:

# 1. str  -> text, always inside quotes
my_name = "Rahul"

# 2. int  -> whole numbers (no decimal point)
my_age = 22

# 3. float -> numbers with a decimal point
my_height = 5.9

# 4. bool -> True or False (note the capital letter)
is_learning = True

# print() can show several things separated by commas.
print("Name:", my_name)
print("Age:", my_age)
print("Height:", my_height)
print("Currently learning?", is_learning)

# type() tells you what kind of value a variable holds.
print("The type of my_name is", type(my_name))
print("The type of my_age is", type(my_age))

# You can change a variable later — it's just a label you can move.
my_age = my_age + 1
print("Next year I will be", my_age)
