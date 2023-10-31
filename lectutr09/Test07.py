import Test06   #๊User(Dew)-defing module
import math     #Build-in module
# import test08
from Test08 import calcircleArea, calsquareArea, calTriangleArea

print(f'f ผลรวมของ 10 + 20 ='(Test06.sumNumber(10,20)))

Test06.showhi()

print(f'ราคาสินค้า 20000 ภาษีเป็นเงิน {2000 * Test06.VAT}')

print(f'7 ยกกำลัง 15 มีค่า {math.pow(7, 15)}')

print(f'พื้นที่ของวงลกม รัศมี 3 มีค่า {math.pi * math.pow(3, 2)}')

print(f'พื้นที่ของวงลกม รัศมี 8 มีค่า {calcircleArea(8)}')

print(f'พื้นที่ของสี่เหลี่ยม กว้าง 10 ยาว 5 มีค่า {calcircleArea(10, 5)}')