#function แบบที่ 2 - Have parameters/No return
#parameters คือ เป็นตัวแปรประเภทหนึ่ง เอาไว้รับค่าคำมาใช้เฉพาะในฟังก์ชั้นนั้นๆ เท่านั้น

def funcA( x, y ) :
    print(f'X is {x}')
    print(f'Y is {y}')
    print(f'Sum {x} + {y} = {x+y}')

funcA(10, 20) #call function #argment อาร์คิวเมนต์ คือค่าที่ส่งให้ parameters
funcA(1, 4)
print('DTI..........')
funcA(5, 5)