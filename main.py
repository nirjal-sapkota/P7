my_dict = {}
my_dict = {1 :'Apple', 2:'ball'}
my_dict = {'name': "Nayan", 1: [2, 4, 3]}
my_dict = {'name': "Nirjal", 'age': 15}

print(my_dict['name'])
print(my_dict.get('age'))

my_dict['age'] = 16
print(my_dict)

my_dict['address'] = 'Hornsby'
print(my_dict)

my_dict.pop('age')
print(my_dict)

print('Addrss :', my_dict.get('address'))

my_dict.clear()
print(my_dict)