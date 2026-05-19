# Exercises: Level 1

# 1. Get user input using input("Enter your age: ").
# If user is 18 or older, give feedback:
# You are old enough to drive.
# If below 18, give feedback to wait for the missing amount of years.
# Output:
# Enter your age: 30
# You are old enough to learn to drive.
# Output:
# Enter your age: 15
# You need 3 more years to learn to drive.
num = int(input("Enter your age "))
if num >= 18:
    print("You are old enough to drive")
else:
    years_left = 18 - num
    print(f"you need {years_left} years to drive")

# 2. Compare the values of my_age and your_age using if … else.
# Who is older (me or you)?
# Use input("Enter your age: ") to get the age as input.
# You can use a nested condition to print 'year' for 1 year difference in age,
# 'years' for bigger differences, and a custom text if my_age = your_age.
# Output:
# Enter your age: 30
# You are 5 years older than me.
my_age = 18 
your_age = int(input("Enter your age: "))

if my_age > your_age:
    difference = my_age - your_age
    print(f"the difference between both is {difference} years")
else:
    difference = your_age - my_age
    print(f"the difference between both is {difference} years")


# 3. Get two numbers from the user using input prompt.
# If a is greater than b, return a is greater than b.
# If a is less than b, return a is smaller than b.
# Else, a is equal to b.
# Output:
# Enter number one: 4
# Enter number two: 3
# 4 is greater than 3
a = int(input("pick a number for a "))
b = int(input("pick a number for b "))

if a > b:
    print("a is grater than b")
if a < b:
    print("b is grater than a")
if a == b:
    print("both are equal")

# Exercises: Level 2

# 1. Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
student_grade = int(input("Enter your grade "))
if student_grade >= 90 and student_grade <= 100:
    grade = "A"
    print(f"Your grade is {grade}")
elif student_grade >= 80 and student_grade <= 89:
    grade = "B"
    print(f"Your grade is {grade}")
elif student_grade >= 70 and student_grade <= 79:
    grade = "C"
    print(f"Your grade is {grade}")
elif student_grade >= 60 and student_grade <= 69:
    grade = "D"
    print(f"Your grade is {grade}")
elif student_grade <= 59:
    grade = "F"
    print(f"Your grade is {grade}")


# 3. The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
# If a fruit doesn't exist in the list, add the fruit to the list and print the modified list.
# If the fruit exists, print('That fruit already exist in the list')
fruit = input("Enter a fruit: ")

if fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(fruit)
    print(fruits)

# Exercises: Level 3

# 1. Here we have a person dictionary. Feel free to modify it!
person = {
     'first_name': 'Asabeneh',
     'last_name': 'Yetayeh',
     'age': 250,
     'country': 'Finland',
     'is_married': True,
     'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
     'address': {
         'street': 'Space street',
         'zipcode': '02210'
    }
}

# Check if the person dictionary has skills key.
# If so, print out the middle skill in the skills list.

# Check if the person dictionary has skills key.
# If so, check if the person has 'Python' skill and print out the result.


# If a person skills has only JavaScript and React,
# print('He is a front end developer').

# If the person skills has Node, Python, MongoDB,
# print('He is a backend developer').

# If the person skills has React, Node and MongoDB,
# print('He is a fullstack developer').

# Else print('unknown title').

# For more accurate results more conditions can be nested!

# If the person is married and if he lives in Finland,
# print the information in the following format:
# Asabeneh Yetayeh lives in Finland. He is married.

if "skills" in person:
    print("Python" in person["skills"])

    skills = person["skills"]

    if skills == ["JavaScript", "React"]:
        print("He is a front end developer")
    elif "Node" in skills and "Python" in skills and "MongoDB" in skills:
        print("He is a backend developer")
    elif "React" in skills and "Node" in skills and "MongoDB" in skills:
        print("He is a fullstack developer")
    else:
        print("unknown title")

if person["is_married"] == True and person["country"] == "Finland":
    print(f"{person['first_name']} {person['last_name']} lives in Finland. He is married.")