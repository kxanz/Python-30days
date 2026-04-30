# Day 5 Exercises - Lists
# Source: 30 Days Of Python Day 5 list exercises you uploaded. :contentReference[oaicite:0]{index=0}

# =========================
# Exercises: Level 1
# =========================

# 1. Declare an empty list
# Hint: use [] or list()
from calendar import firstweekday


lst = list()
print(len(lst))
lst = []
# 2. Declare a list with more than 5 items
# Hint: example: names, foods, numbers, etc.
lst = ['banana', 'apple', 'kiwi', 'potato', 'car']
# 3. Find the length of your list
# Hint: use len()
print(len(lst))
# 4. Get the first item, the middle item and the last item of the list
# Hint:
# first item -> index 0
# middle item -> len(list) // 2
# last item -> index -1
first = lst[0]
middle = lst[len(lst)//2]
last = lst[-1]
print(first)
print(middle)
print(last)
# 5. Declare a list called mixed_data_types
# Put your: name, age, height, marital status, address
# Hint: a list can hold strings, numbers, booleans, etc.
mxd = ['luis', 21, 6.0, False, 'texas']
# 6. Declare a list variable named it_companies
# Add: Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
its_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IMB', 'Oracle', 'Amazon']
# 7. Print the list using print()
print(its_companies)
# 8. Print the number of companies in the list
# Hint: len(it_companies)
print(len(its_companies))
# 10. Print the list after modifying one of the companies
# Hint: use index assignment like list[index] = "new value"
its_companies[0] = 1
print(its_companies)
# 11. Add an IT company to it_companies
# Hint: append() adds to the end
its_companies.append(5)
print(its_companies)
# 12. Insert an IT company in the middle of the companies list
# Hint: insert(index, value)
its_companies.insert(-1, '3')
print(its_companies)
# 13. Change one of the it_companies names to uppercase (IBM excluded!)
# Hint: choose any company except IBM, then use .upper()
its_companies[1] = its_companies[1].upper()
# 14. Join the it_companies with a string '#; '
# Hint: use "#; ".join(it_companies)
print("#; ".join(its_companies[1]))
# 15. Check if a certain company exists in the it_companies list
# Hint: use "company" in it_companies
print('IMB' in its_companies)
# 16. Sort the list using sort() method
# Hint: sort() changes the original list
strs = ['Apple', 'Potato', 'Kiwi', "Banana"]
strs.sort()
print(strs)
# 17. Reverse the list in descending order using reverse() method
# Hint: reverse() flips the current order
strs.sort(reverse=True)
print(strs)
# 18. Slice out the first 3 companies from the list
# Hint: list[:3]
slc = strs[0:3]
print(slc)
# 19. Slice out the last 3 companies from the list
# Hint: list[-3:]
slx = strs[-3:-1]
print(slx)
# 20. Slice out the middle IT company or companies from the list
# Hint: if odd length -> one middle item
# if even length -> two middle items

# 21. Remove the first IT company from the list
# Hint: pop(0) or del list[0]
del strs[0]
print(strs)
# 23. Remove the last IT company from the list
# Hint: pop() removes the last item
strs.pop()
print(strs)
# 24. Remove all IT companies from the list
# Hint: clear()
strs.clear()
print(strs)
# 25. Destroy the IT companies list
# Hint: del it_companies
del its_companies
# 26. Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
# Hint: use + or extend()
front_end.extend(back_end)
print(front_end)
# 27. Copy the joined list and assign it to full_stack
# Then insert Python and SQL after Redux
# Hint:
# - use copy()
# - find the index of Redux
# - insert after that index
full_stack = front_end.copy()
print(full_stack)
redux = front_end[4]
full_stack.insert(9, redux)
print(full_stack)
# =========================
# Exercises: Level 2
# =========================

# 1. Given this list of ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
# a. Sort the list and find the min and max age
# Hint: sort(), min(), max()
ages.sort()
print(ages)
# b. Add the min age and max age again to the list
# Hint: append() twice
ages.append(min(ages))
ages.append(max(ages))
print(ages)
# c. Find the median age
# Hint: sort first
# if length is even, get the two middle values and divide by 2
n = len(ages)
middle1 = ages[n//2 - 1]
middle2 = ages[n//2]
median = (middle1 + middle2) / 2

print(median)
# d. Find the average age
# Hint: sum(ages) / len(ages)
sums = sum(ages)
l = len(ages)
avg = sums / l
print(avg)

# f. Compare abs(min - average) and abs(max - average)
# Hint: use abs()
mins = min(ages)
maxs = max(ages)
avg = sum(ages) / len(ages)

diff_min = abs(mins - avg)
diff_max = abs(maxs - avg)

print(diff_min)
print(diff_max)

# 4. Unpack the first three countries and the rest as scandic countries
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
countries_one, countries_two, countries_three, *scandic = countries
print(scandic)
# Hint:
# first, second, third, *scandic = countries hf