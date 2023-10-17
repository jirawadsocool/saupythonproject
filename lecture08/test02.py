# list มีลำดับ
my_list = [10, 20, 10, 'hi', True[20, 'hello'],(10,20),(10,20)]

# tuple มีลำดับ
my_tuple = (10, 20, 10, 'hi', True(20, 'hello'),(10,20),(10,20))

# set ไม่มีลำดับ
my_set = {10, 20, 10, 'hi', True,(10,20)}
    # key คือ associative

# Dictionay ------> key:value / key-> string-number / vulue -> everything
my_dict = {'name' : 'สมชาย', 'age':20, 555:999, 'fing':True }
print(my_dict['name'])
print(my_dict['age'] + my_dict[555])
my_dict['name'] = 'สมหญิง'
my_dict['major'] = 'DTI'
print(my_dict)
my_dict.pop('name')
my_dict.pop(555)
print(my_dict)

for date in my_dict :
    pass

for date in my_dict.keys() :
    print(date, end=' ')

print()

for date in my_dict.values :
    print(date, end=' ')

my_dict1 = {'a':10, 'b':20, 'c':30}

my_dict2 = my_dict1

my_dict3 = my_dict.copy()

print()
print(my_dict2)
print(my_dict3)
my_dict2['a'] = 999
my_dict3['a'] = 999
print('---------------')
print(my_dict1)
print(my_dict2)
print(my_dict3)
