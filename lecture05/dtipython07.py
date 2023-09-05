#โปรแกรมคำนวณการหาพื้นที่วงกลม เส้นรอบวงกลม และปริมาณของวงกลม จากรัศมีที่ป้อนโดยผู้ใช้ทางแป้นพิมพื และแสดงผลพื้นที่ เส้นรอบ และปริมาณ

#ขอ 5 ฟังก์ชัน
import math
#inputRadius
def inputRadius() :
    # r = input('ป้อนรัศมี : ')
    # return

    # r = float(input('ป้อนรัศมี : ') )
    # return r

    #return input ('ป้อนรัศมี : ')

    return float( input('ป้อนรัศมี : ') )


#calAreaCircle
def calAreaCirle ( r ) :
    #area = math.pi * r ** 2
    #area = math.pi * r * r
    # area = math.pi * math.pow(r, 2)
    # return area
    return math.pi * math.pow(r, 2)

#calRoundCirle 2 * PI * r
def calRoundCirle ( r ) :
    


#calCubeCirle 4 / 3 * PI * r * r * r


#showResul ขอทั้งหมดทสนิยม 4 ตำแหน่ง
#พื้นที่วงกลมเป็น ???? เส้นรอบวงเป็น ???? ปริมาณตรทรงกลมเป็น ??? (^_-) db (-_^)