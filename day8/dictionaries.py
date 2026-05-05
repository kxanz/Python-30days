# Day 8 Exercises

# 1. Create an empty dictionary called dog
dog = {}

# 3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student_dictionary = {
    'first_name':'luis', 
    'last_name':'munoz', 
    'gender':'male', 
    'martial_status':True,
    'skills':
        ['cpp', 'java', 'javascript'],
    'country':'texas',
    'city':'chicago',
    'adress':3333,
     }

# 4. Get the length of the student dictionary
print(len(student_dictionary))


# 5. Get the value of skills and check the data type, it should be a list
print(type(student_dictionary['skills']))

# 6. Modify the skills values by adding one or two skills
student_dictionary['skills'].append('HTML')
print(student_dictionary['skills'])

# 7. Get the dictionary keys as a list
student_dictionary.keys()
# 8. Get the dictionary values as a list
student_dictionary.values()

# 9. Change the dictionary to a list of tuples using items() method
student_dictionary.items()

# 10. Delete one of the items in the dictionary
student_dictionary.pop('first_name')

# 11. Delete one of the dictionaries
del student_dictionary

# 🎉 CONGRATULATIONS 🎉