# 03_math_operators.py
# Lesson: doing math in Python.
# Run it with:  python 00-python-basics/03_math_operators.py

a = 10
b = 3

# The basic math operators:
print("Addition:        a + b =", a + b)   # 13
print("Subtraction:     a - b =", a - b)   # 7
print("Multiplication:  a * b =", a * b)   # 30
print("Division:        a / b =", a / b)   # 3.333...  (always a float)
print("Floor division:  a // b =", a // b) # 3   (drops the decimal part)
print("Remainder (mod): a % b =", a % b)   # 1   (what's left over)
print("Power:           a ** b =", a ** b) # 1000  (10 to the power 3)

# Order of operations works like in math (use () to be explicit).
result = (a + b) * 2
print("(a + b) * 2 =", result)

# Math is the foundation of AI/ML — every model is just a lot of these
# operations done on numbers. Getting comfortable here pays off later.
