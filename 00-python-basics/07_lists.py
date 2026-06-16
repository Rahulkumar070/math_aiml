# 07_lists.py
# Lesson: lists (and a quick look at dictionaries).
# Run it with:  python 00-python-basics/07_lists.py

# A LIST holds many values in order, inside square brackets [].
scores = [80, 95, 60, 75, 100]
print("All scores:", scores)

# Each item has a position called an INDEX, starting at 0 (not 1!).
print("First score (index 0):", scores[0])
print("Third score (index 2):", scores[2])
print("Last score (index -1):", scores[-1])   # -1 is a shortcut for the last item

# How many items are in the list?
print("Number of scores:", len(scores))

# Add a new item to the end.
scores.append(88)
print("After append:", scores)

# Loop over a list to work with every item.
total = 0
for s in scores:
    total = total + s
print("Total:", total)
print("Average:", total / len(scores))

# Python even has built-in helpers:
print("Highest:", max(scores), " Lowest:", min(scores))

# A DICTIONARY stores labeled pairs: key -> value, inside curly braces {}.
student = {"name": "Rahul", "age": 22, "course": "AIML"}
print("Student name:", student["name"])   # look up a value by its key
print("Student course:", student["course"])
