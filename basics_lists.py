# use lists, dictionaries and tuples
list_num = [9, 99, 999, 9999, 99999]
list_str = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
list_mix = ['Monday', 'Tuesday', 3, 'Thursday', 5]

tuple_mix = (1, "Monday", "Week", 2020)

dict_car = {'Brand': 'Dodge', 'Model': 'Challenger', 'Year': '1969', 'Color': 'Black'}

# Use  get, add, remove elements for list structures

print(list_num.__getitem__(4))

list_str.append('Saturday')
print(list_str)

list_mix.remove(5)
print(list_mix)

