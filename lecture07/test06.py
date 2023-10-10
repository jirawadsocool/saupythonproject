# slicing data in list and tuple

var1 = [10, 20, 'Hello', True, [111, 'Wow'], 'มานะ']

var2 = (10, 20, 'hello', True (111, 'Wow'),'มานะ')

# 20, 'Hello' , True
print( var1[1:4] )
# True, (111, 'wow')
print(var1[:3])
# 'hello', True, [1111, 'wow'], 'มานะ'
print(var1[2:])