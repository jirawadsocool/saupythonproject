def inputCarDetail () :
    carNo = input('ป้อนทะเบียนรถ : ')
    Weight = float( input('ป้อนน้ำหนักรถ : ') )
    return carNo, Weight
def checkCarAndShowWeight(carNo, Weight) :
    if Weight > 1000 :
        print(f'{carNo} น้ำหนักไม่ผ่านเกณฑ์')
    else :
        print(f'{carNo} น้ำหนักรถผ่านเกณฑ์')

print('-----------------------------')
print('--* Truck Checker*--')
print('-----------------------------')
carNo, Weight = inputCarDetail()
print('------------------------------')
checkCarAndShowWeight(carNo, Weight)
print('------------------------------')
