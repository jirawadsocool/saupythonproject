# List Function/tuple function
# len(), min(), max()

varl = [10, 20, 'Hello', True, [111, 'Wow'], 'มานะ']

var2 = (10, 20, 'hello', True (111, 'Wow'),'มานะ')

print(f'ใน var1 มีข้อมูลทั้งหมด {len(varl)} ข้อมูล')
print(f'ใน var2 มีข้อมูลทั้งหมด {len(var2)} ข้อมูล')
# min กับ max ใช้ในข้อมูลคนละชนิดกัน
# print(min(varl)) error
var3 = [10 , 20 ,30 , True, 10, 20]
var4 = (10 , 20 ,30 , True, 10, 20)
print(min(var3))
print(max(var4))