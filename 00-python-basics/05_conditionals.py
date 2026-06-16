# 05_conditionals.py
# Lesson: making decisions with if / elif / else.
# Run it with:  python 00-python-basics/05_conditionals.py

score = 75

# An "if" runs a block of code ONLY when its condition is True.
# The indented lines below the colon ":" belong to that block.
if score >= 90:
    print("Grade: A")
elif score >= 75:        # "elif" = else if: checked only if the above was False
    print("Grade: B")
elif score >= 50:
    print("Grade: C")
else:                    # "else" runs when nothing above matched
    print("Grade: F")

# Comparison operators give you True or False:
#   ==  equal        !=  not equal
#   >   greater      <   less
#   >=  greater/equal  <=  less/equal
print("Is score equal to 75?", score == 75)
print("Is score above 90?", score > 90)

# You can combine conditions with "and" / "or" / "not":
age = 20
has_id = True
if age >= 18 and has_id:
    print("Allowed to enter.")
else:
    print("Not allowed.")
