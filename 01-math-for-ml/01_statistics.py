# 01_statistics.py
# Math for ML — Lesson 1: basic statistics (describing data).
# We compute everything "by hand" with plain Python so you see how it works.
# Run it with:  python 01-math-for-ml/01_statistics.py

# Imagine these are test scores of 7 students.
scores = [55, 70, 70, 80, 90, 95, 100]

# ---- MEAN (the average) ----
# Add everything up, divide by how many there are.
total = sum(scores)
count = len(scores)
mean = total / count
print(f"Scores: {scores}")
print(f"Mean (average): {mean}")   # the 'center' of the data

# ---- MEDIAN (the middle value) ----
# Sort the numbers, then pick the middle one.
ordered = sorted(scores)
middle_index = count // 2
if count % 2 == 1:                 # odd number of values -> one middle value
    median = ordered[middle_index]
else:                             # even -> average the two middle values
    median = (ordered[middle_index - 1] + ordered[middle_index]) / 2
print(f"Median (middle value): {median}")

# ---- MODE (the most common value) ----
# The value that appears most often.
mode = max(scores, key=scores.count)
print(f"Mode (most frequent): {mode}")

# ---- VARIANCE & STANDARD DEVIATION (how spread out the data is) ----
# Variance: average of the squared distances from the mean.
squared_diffs = [(x - mean) ** 2 for x in scores]   # list comprehension!
variance = sum(squared_diffs) / count
# Standard deviation: square root of the variance (back to normal units).
std_dev = variance ** 0.5
print(f"Variance: {variance:.2f}")
print(f"Standard deviation: {std_dev:.2f}")

# WHY THIS MATTERS IN ML:
# - Mean/median describe the 'typical' value in your data.
# - Standard deviation tells you how noisy or spread out it is.
# - Models care a lot about the center and spread of data, and you'll
#   'normalize' data using exactly these numbers later on.
