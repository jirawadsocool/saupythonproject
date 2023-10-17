# list
my_list = [10, 20, 10, 'hi', True[20, 'hello']]
print(my_list)
print(len(my_list))

# tuple
my_tuple = (10, 20, 10, 'hi', True(20, 'hello'))
print(my_tuple)
print(len(my_tuple))

# set
my_set = {10, 20, 10, 'hi', True}
print(my_set)
print(len(my_set))

for date in my_set :
    print(date, end='/')

print('--------------------------------------')

list_fr_set = list( my_set )
print(list_fr_set)
my_set = set(list_fr_set)
print(my_set)

set.clear()
print(len(my_set))

my_set1 = {10, 20, 30, 'Hi'}
my_set2 = {10, 'hello', 'Hi', True}

my_set1.add(999)
print(my_set1)
my_set1.remove('hi')
print(my_set1)

print(my_set1.intersection(my_set2))
print(my_set1.union(my_set2))

# len, with, max
print(min(my_set2))