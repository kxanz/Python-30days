# Day 4 Exercises (Strings)
# Keep each exercise under its own comment block so you don't get lost.

# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
# Hint: you can use + with spaces in between
t = 'Thirty '
d = ' days'
o = ' Of'
p = ' Python'
full = t + d + o + p
print(full)
# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# Same idea as above
coding = 'Coding ' 'For' " All"
print(coding)
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# Store the string first, then reuse it in later questions
company = "Coding For All"
# 4. Print the variable company using print().
# Very small one
print(company)
# 5. Print the length of the company string using len() method and print().
# len(company)
print(len(company))
# 6. Change all the characters to uppercase letters using upper() method.
# Call the method on the string variable
print(company.upper())
# 7. Change all the characters to lowercase letters using lower() method.
# Opposite of upper()
print(company.lower())
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
# You can print each one on a separate line
print(company.capitalize())
print(company.title())
print(company.swapcase())
# 9. Cut(slice) out the first word of Coding For All string.
# Think about where the first word ends
first_word = company[0:6]
print(first_word)
# 10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
# index/find gives position; 'in' gives True/False
print("Coding" in company)
# 11. Replace the word coding in the string 'Coding For All' to Python.
# Watch capitalization carefully
print(company.replace('Coding', 'Python'))
# 12. Change "Python for Everyone" to "Python for All" using the replace method or other methods.
# This is a clean replace() practice question
print(company.replace("Coding For All", 'Pythong For Everyone'))
# 13. Split the string 'Coding For All' using space as the separator (split()) .
# split() by default uses spaces, but you can also pass " "
print(company.split())
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# The result should be a list
company_all = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(company_all.split())
# 15. What is the character at index 0 in the string Coding For All.
# Index 0 means the first character
print(company[0:1])
# 16. What is the last index of the string Coding For All.
# Last index usually means len(string) - 1
print(len(company)-1)
# 17. What character is at index 10 in "Coding For All" string.
# Count carefully including spaces
print(company[10])
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# Take the first letter of each word
text = 'Python For Everyone'
words = text.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# index() returns the position
print(company.index('C'))
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# Same method as above
print(company.index('F'))
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# rfind searches from the right side
print(company.rfind('l'))
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# Put the sentence in a variable first to make life easier
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.index('because'))
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# rindex is like searching from the right
sentence_one = 'You cannot end a sentence with because because because is a conjunction'
print(sentence_one.rindex('because'))
# 25. Slice out the phrase 'because because because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# Find the start and end, then slice
sentence_two = 'You cannot end a sentence with because because because is a conjunction'
start = sentence_two.find('because')
end = sentence_two.rfind('because') + len('because')
print(sentence_two[start:end])
# 26. Find the position of the first occurrence of the word 'because' in the following sentence:
# 'You cannot end a sentence with because because because is a conjunction'
# This repeats an earlier one, so you can reuse the same idea
print(sentence.index('because'))
# 28. Does 'Coding For All' start with a substring Coding?
# startswith()
print(company.startswith('Coding'))
# 29. Does 'Coding For All' end with a substring coding?
# endswith()
# Watch the lowercase c here
print(company.endswith('Coding'))
# 30. '   Coding For All      '  , remove the left and right trailing spaces in the given string.
# strip() removes spaces from both ends
company_new = '   Coding For All      '
print(company_new.strip())

# 31. Which one of the following variables return True when we use the method isidentifier():
a = '30DaysOfPython'
b = 'thirty_days_of_python'
# Try isidentifier() on both
print(a.isidentifier())
print(b.isidentifier())
# 32. The following list contains the names of some of python libraries:
a = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space string.
formated_a = ' # '.join (a)
print(formated_a)
# 33. The following list contains the names of some of python libraries:
b = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
# Join the list with a hash with space string.
# Yes, this is repeated in your sheet, so you can do it again or leave a note
formatb = ' # ' .join(a)
print(formatb)
# 34. Use the new line escape sequence to separate the following sentences.
# New line escape sequence is \n
print('I am enjoying this challenge.\nI just wonder what is next.')


# 35. Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Tab escape sequence is \t
print('Name\t Age\t Country\t City \nAsabeneh\t 250\t Finland\t Helsinki\n')


# 🎉 CONGRATULATIONS !
# Finish these one by one. Reuse variables when you can so the file stays clean.