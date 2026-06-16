# 08_functions.py
# Lesson: functions — reusable blocks of code.
# Run it with:  python 00-python-basics/08_functions.py

# A FUNCTION is a named recipe you can run whenever you want.
# "def" defines it. The words in (parentheses) are inputs called PARAMETERS.
def greet(name):
    print("Hello,", name, "- welcome back!")

# "Calling" the function runs its code. We can reuse it as often as we like.
greet("Rahul")
greet("Asha")

# Functions can RETURN a value so we can use the result elsewhere.
def add(x, y):
    return x + y

answer = add(10, 5)
print("10 + 5 =", answer)

# A more useful example: average of a list of numbers.
def average(numbers):
    return sum(numbers) / len(numbers)   # sum() and len() are built in

my_scores = [80, 95, 60, 75, 100]
print("Average score:", average(my_scores))

# Why functions matter: in ML you'll constantly reuse steps like
# "prepare the data", "train the model", "score the model". Functions
# keep that code organized and repeatable instead of copy-pasted.
