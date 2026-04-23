# Day 3 Exercises

# 1. Declare:
age = 18
height = 1.75
is_student = True

# 2. Check the data type of:
# age
print(type(age))
# height
print(type(height))
# is_student
print(type(is_student))


# 3. Compare the following values (print True or False):
print(4 > 3)
print(4 >= 3)
print(4 < 3)
print(4 <= 3)
print(4 == 4)
print(4 != 4)

# 4. Find the length of:
print(len("python"))
print(len("dragon"))
# Check if the lengths are equal

# 5. Compare:

print(len("python") == len("dragon"))
print(len("python") != len("dragon"))



# 6. Use logical operators:
print(True and False)
print(True or False)
print(not(True and True))

# 7. Check:
# 4 is greater than 3 AND 10 is less than 12
print(4 > 3 and 10 < 12)
# 4 is greater than 3 OR 10 is greater than 12
print(4 > 3 or 10 > 12)
# NOT (4 is greater than 3)
print(not(4 > 3))


# 8. Use comparison:
print(len("python") > len("dragon"))


# 9. Check:
# "on" is in both "python" and "dragon"
print("on" in "python") and ("on" in "dragon")

# 10. Check:
# Is the floor division of 7 by 3 equal to the int of 2.7?
print(7 // 3) #2

# 11. Write a program that asks the user:
# "Enter number of years you have lived: "
# Then calculate how many seconds the person has lived
# (Hint: 1 year = 365 days)
years_lives = input("How many years you have lives: ")
result = int(years_lives) * 365
print(f"Days you lives: {result}")

# 12. Print the following table:
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
#
# Hint: look for a pattern (n, n^0, n^1, n^2, n^3)
for n in range(1, 6):
    #1-5
    print(n, n**0, n**1, n**2, n**3)
    #n to the power of **