# 04_input.py
# Lesson: getting input from the user.
# Run it with:  python 00-python-basics/04_input.py

# input() pauses the program and waits for the user to type something.
# Whatever they type comes back as a str (text).
name = input("What's your name? ")
print("Nice to meet you,", name)

# input() ALWAYS gives text, even if the user types a number.
# To do math with it, we must convert it: int() for whole numbers.
age_text = input("How old are you? ")
age = int(age_text)   # convert the text "22" into the number 22

print("In 5 years you will be", age + 5)
