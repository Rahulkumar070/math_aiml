# 09_strings.py
# Bonus lesson: working with text (strings) and f-strings.
# Run it with:  python 00-python-basics/09_strings.py

text = "Machine Learning"

# Strings have handy METHODS (actions you call with a dot).
print("Upper case:", text.upper())        # MACHINE LEARNING
print("Lower case:", text.lower())        # machine learning
print("How many letters:", len(text))     # counts spaces too
print("Replace:", text.replace("Machine", "Deep"))  # Deep Learning

# SLICING: grab part of a string by position [start:end] (end not included).
print("First 7 letters:", text[0:7])      # Machine
print("From letter 8 on:", text[8:])      # Learning

# .split() breaks text into a list wherever it finds a space.
words = text.split(" ")
print("Split into words:", words)         # ['Machine', 'Learning']

# F-STRINGS: the cleanest way to put variables inside text.
# Put an f before the quotes, then write variables inside { }.
name = "Rahul"
age = 22
print(f"Hi, I'm {name} and I'm {age} years old.")

# You can even do math inside the { }:
print(f"In 5 years I'll be {age + 5}.")
