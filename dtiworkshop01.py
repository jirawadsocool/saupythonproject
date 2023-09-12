#dtiworkshop01.oy
#โปรแกรมคำนวณหาพื่นที่สามเหลี่ยมโดยรับค่าฐานและสูงทางแป้นพิมพ์และแสดงที่สามเหลี่ยมที่คำนวณได้ทางหน้าจอ

#วิเคราะห์
#มองหา featuer การทำงานมีอะไรบ้าง เพื่อจะไปส้รางเป็น funtion
#1. รับค่า ฐาน สูง
#2. คำนวณพื้นที่ และแสดงผลออกมา

def inputBaseHigh() :
    base = float( input('ป้อนฐาน : ') )
    high = float( input('ป้อนสูง : ') )
    return base, high

def calAndShowTriangleArea (base, high) :
    area = base * high / 2
    print(f'สามเหลี่ยมฐาน {base:.2f} สูง {high:.2f} มีพื้นที่ {area:.2f}')

print('-----------------------------')
print('--*Calculate Triangle Area*--')
print('-----------------------------')
base, high = inputBaseHigh()
print('-----------------------------')
calAndShowTriangleArea(base, high)
print('-----------------------------')