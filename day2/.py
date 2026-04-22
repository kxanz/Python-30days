# Day 2 - Level 2 Exercises

# 1. Create variables:
# first_name
first_name = "luis"
# last_name
last_name = "munoz"
# country
country = "texas"
# age
age = 21
# is_student
is_student = True


# 2. Use type() to check the data type of all your variables
print(type(first_name))
print(type(age))
print(type(is_student))


# 3. Use len() to find the length of your first name
# Use len() to find the length of your last name
# Compare both lengths
print(len(first_name))
print(len(last_name))
print(len(first_name) - len(last_name))

# 4. Create:
num_one = 5
num_two = 4
#
# Find:
# total
print(num_one + num_two)
# diff
print(num_one - num_two)
# product
print(num_one * num_two)
# division
print(num_one / num_two)
# remainder
print(num_one % num_two)
# exp
print(num_one ** num_two)
# floor_division
print(num_one // num_two)


# 5. The radius of a circle is 30
# Calculate: 
# area_of_circle
pi = 3.14
radius = float(input("Enter radius"))
erea_of_circle = pi * radius * radius
print(f"Your erea of circle is: {erea_of_circle}" )
# circum_of_circle
pi = 3.14
radius = float(input("Enter  radius: "))
circum_of_circle = 2 * pi * radius
print("The circumference is" , circum_of_circle)

# 7. Ask the user to enter:
# first name
first_n = input("Enter your first name: ")
# last name
last_n = input("Enter your last name: ")
# country
country_n = input("Enter your country: ")
# age
age_n = input("Enter your age: ")

print(f"Your full name: {first_n} {last_n} Your country: {country_n} Your age: {age_n}")


# 8. Run:
# help('keywords')
#
# Look at the Python reserved words