# List Method
var1 = [10, 20, 'hello', True, [111, 'wow'], 'มานะ']
# append
var1.append(555)
var1.append({'Hi', 'hey', 999})
print(var1)
# extent เพิ่มแต่ละข้อมูล
var1.extend({10, 20, 30})
print(var1)
# remove
var1.remove('hello')
var1.remove(10)
print(var1)
# -------------
var2 = [10, 20, 'hello']
# insert
var2.insert(2, 'hi')
print(var2)
# pop
var2.pop()
print(var2) # [10, 20, 'hi']
var2.pop(1)
print(var2)
# index
print(var2.index('hi'))
# count
print(var1.count(10))
var3 = [10, 10, 20, 'hi', 10,'hi']
print(f'ใน var3 มี 10 ทั้งหมด {var3.count(10)} ตัว')
print(f'ใน var3 มี 10 ทั้งหมด {var3.count("hi")} ตัว')
print(f"ใน var3 มี 10 ทั้งหมด {var3.count('hi')} ตัว")
print('hi \'SAU\'')
print('hi')
print('hi')
print('hi "DIT"')
# เมธอดตอ่ไปนี้ใฃ้ได้ฉะเพราะข้อมูลที่เป็นประเภทเดียวกันเท่านั้น
# sort
var4 = [10, 10, 20, 'hi', 10, 'hi']
# var4.sort() error
var5 = [99, 34, 635, 3423, 99]
print(var5)
var5.sort()
print(var5)
var5.sort(reverse=True)
print(var5)