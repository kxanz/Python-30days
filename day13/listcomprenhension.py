# Filter only negative and zero in the list using list comprehension

numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

filter_numbers = [i for i in numbers if i <= 0]
print(filter_numbers)

# Flatten the following list of lists of lists to a one dimentional list:

list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

flat_list = [number for i in list_of_lists for number in i]
print(flat_list)

list_of_tuples = [(i, i * i) for i in range(100000)]
print(list_of_tuples)

#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
countries_output = [number for i in countries for number in i ]
print(countries_output)

#5 Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [
    [c[0][0].upper(), c[0][0].upper()[:3], c[0][1].upper()] for c in countries]

#5.1 Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
result = [
    {'country': country.upper(), 'city': city.upper()}
    for [(country, city)] in countries
]

#6 Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
result = [f'{first} {last}' for [(first , last)] in names]

#7
def slope(x):
    return lambda n : x * n

cube = slope(4)(5)
print(cube)