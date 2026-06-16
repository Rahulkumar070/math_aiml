# 06_loops.py
# Lesson: repeating things with loops.
# Run it with:  python 00-python-basics/06_loops.py

# A FOR loop repeats once for each item in a sequence.
# range(1, 6) gives the numbers 1, 2, 3, 4, 5  (the end number is not included).
print("Counting with a for loop:")
for number in range(1, 6):
    print("  number is", number)

# A common use: add up numbers (a "running total").
total = 0
for number in range(1, 6):
    total = total + number   # add each number to the total
print("The sum of 1..5 is", total)

# A WHILE loop repeats as long as its condition stays True.
print("Counting down with a while loop:")
countdown = 3
while countdown > 0:
    print("  ", countdown)
    countdown = countdown - 1   # IMPORTANT: change the value, or it loops forever
print("  Liftoff!")

# Loops are everywhere in ML: training a model means looping over data
# many times, adjusting numbers a little each pass.
