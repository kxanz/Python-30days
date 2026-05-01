# Day 7 Exercises (Sets)

# =========================
# Given Data
# =========================

it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# =========================
# Exercises: Level 1
# =========================

# 1. Find the length of the set it_companies
# Hint: use len()
print(len(it_companies))

# 2. Add 'Twitter' to it_companies
# Hint: use add()
it_companies.add("Twitter")
print(it_companies)
# 3. Insert multiple IT companies at once to the set it_companies
# Hint: use update() with a list or another set
it_companies.update(A)
print(it_companies)

# 4. Remove one of the companies from the set it_companies
# Hint: use remove() or discard()
it_companies.remove('Twitter')
print(it_companies)

# 5. What is the difference between remove and discard
# 
# - remove() → gives error if item not found
# - discard() → no error

# =========================
# Exercises: Level 2
# =========================

# 1. Join A and B
C = B.union(A)
print(C)

# 2. Find A intersection B
A.intersection(B)

# 3. Is A subset of B
A.issubset(B)

# 4. Are A and B disjoint sets
A.isdisjoint(B)


# 6. What is the symmetric difference between A and B
A.symmetric_difference(B)

# 7. Delete the sets completely
del A
del B

# =========================
# Exercises: Level 3
# =========================

# 1. Convert the ages to a set and compare the length of the list and the set
st = set(age)
print(len(age))
print(len(st))
# 2. Explain the difference between:
# string, list, tuple and set

# string → ordered, immutable (cannot change), uses quotes
# list → ordered, mutable (can change), allows duplicates
# tuple → ordered, immutable, allows duplicates
# set → unordered, no index, no duplicates, mutable (can add/remove)

# 3. Count unique words in the sentence:
sentence = "I am a teacher and I love to inspire and teach people"

words = sentence.split()     # step 1
unique_words = set(words)    # step 2
count = len(unique_words)    # step 3



# 🎉 CONGRATS — Sets are super important for interviews (especially duplicates problems)