class DTITest01 :
    pass

class DTITest02 :
    # data/attribute/proprty/field คือ ตัวแปรประเภทหนึ่ง
    infoA = ""
    infoB = 20

    # method คือ ฟังก์ประเภทหนึ่ง
    def showHi(self) :
        print("hi........")

    def showInfoAndB(self) :
        print(self.infoA)
        print(self.infoB)

# สร้าง object
objA = DTITest02()
objB = DTITest02()
sombat = DTITest02()

objA.infoA = 'xxxxx'
objB.infoB = 100

print(objA.infoB + objB.infoB)

sombat.showInfoAndB()