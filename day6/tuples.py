# ----------------------------------------
# LEVEL 1   TUPLES
# ----------------------------------------

# 1. Create an empty tuple
from typing import Literal


from math import fabs


luis = ()
munoz = tuple()
# 2. Create a tuple containing names of your sisters and your brothers
family = ('luis', 'john', 'Vee', 'Jennifer')
# 3. Join brothers and sisters tuples and assign it to siblings
brothers = family[0:2]
sisters = family[-2: -1]
siblings = brothers + sisters

print(siblings)

# 4. Find how many siblings you have and display the result

print(len(siblings))

# 5. Modify the siblings tuple by adding the name of your father and mother
#    Assign the result to family_members
parents = ('mom', 'dad')
family_members = siblings + parents

# ----------------------------------------
# LEVEL 2
# ----------------------------------------


# 7. Create three tuples: fruits, vegetables, and animal products
fruits = ('banana', 'apple', 'orange')
vegetables = ('celery', 'squash')
animalP = ('catfood', 'dogfood')

# 8. Join the three tuples into a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animalP

# 9. Convert the food_stuff_tp tuple into a list called food_stuff_lt
food_stuff_lt = list(food_stuff_tp)

# 10. Slice out the middle item or items from the food_stuff_tp tuple
#     or from the food_stuff_lt list
mid = len(food_stuff_lt) // 2
middle_items = food_stuff_lt[mid:mid+1]
print(middle_items)

# 11. Slice out the first three items and the last three items
#     from the food_stuff_lt list
slide_first = food_stuff_lt[:3]
slice_last = food_stuff_lt[-3:]

# 12. Delete the food_stuff_tp tuple completely
del food_stuff_tp

# ----------------------------------------
# 13. Check if an item exists in tuple
# ----------------------------------------

# Given:
nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

# Check if 'Estonia' is a nordic country and display the result
print('Estonia' in nordic_countries)

# Check if 'Iceland' is a nordic country and display the result
print('Iceland' in nordic_countries)