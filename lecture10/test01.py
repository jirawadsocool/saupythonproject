try :
    num1 = int(input ("input number 1 : "))
    num2 = int(input ("input number 2 : "))

    reauit1 = num1 * num2
    reauit2 = num1 / num2

    print (f'{num1} x {num2} = {reauit1}')
    print (f'{num1} x {num2} = {reauit2}')
except ValueError :
    print (f'ตรวจสอบการป้อนข้อมูลผิดพลาดเนื่องจากป้อนข้อมูลไม่ถูกต้อง')
except ZeroDivisionError :
    print(f'ตรวจสอบการป้อนข้อมูล ตัวเลขที่ 2 ห้ามเป็น 0')
except Exception :
    print(f'มีข้อผิดพลาดเกิดขึ้น กรุณาติดต่อ 02245454 ทีม IT')
finally :
    print('wow wow wow')