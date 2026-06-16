# 10_list_comprehensions.py
# Bonus lesson: list comprehensions — building lists in one clean line.
# Run it with:  python 00-python-basics/10_list_comprehensions.py

numbers = [1, 2, 3, 4, 5]

# THE OLD WAY: build a new list with a loop (perfectly fine, just longer).
squares_old = []
for n in numbers:
    squares_old.append(n * n)
print("Squares (loop):", squares_old)

# THE COMPREHENSION WAY: same result, one line.
# Read it as: "n * n  for each n  in numbers".
squares_new = [n * n for n in numbers]
print("Squares (comprehension):", squares_new)

# You can add a CONDITION to filter items.
# Read it as: "n  for each n in numbers  IF n is even".
evens = [n for n in numbers if n % 2 == 0]
print("Even numbers only:", evens)

# It works on text too.
words = ["machine", "learning", "ai"]
shouted = [w.upper() for w in words]
print("Shouted:", shouted)

# Why this matters: ML code is full of "transform every item in this data"
# steps. Comprehensions make those short and readable — you'll see them a lot.
