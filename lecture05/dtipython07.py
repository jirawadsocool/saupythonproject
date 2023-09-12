#โปรแกรมคำนวณการหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาณของวงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพื และแสดงผลพื้นที่ เส้นรอบ และปริมาณ

#ขอ 5 ฟังก์ชัน
import math
#inputRadius
def inputRadius() :
    return float( input('ป้อนรัศมี : ') )

def calAreaCirle ( r ) :
    return math.pi * r * r

def calRoundCirle ( r ) :
    return 2 * math.pi * r

#showResul ขอทั้งหมดทสนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ???? เส้นรอบวงเป็น ???? ปริมาณตรทรงกลมเป็น ??? (^_-) db (-_^)

def showResul( ) :
    r = inputRadius()
    print(f"พื้นที่วงกลม {calAreaCirle(r):.4f} เส้นรอบวง {calRoundCirle(r):.4f} ปริมาตรทรงกลม {callable(r):.4f} ")

showResul()