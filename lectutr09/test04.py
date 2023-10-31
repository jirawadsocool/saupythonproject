# คุณสมบัติ Encagsulation (ห่่อหุ่ม)
class Dtitest05 :
    # data
    infoA = 10 #ไม่ห่อหุ้มกินที่ร้าน หรือ ไม่ได้ Encap
    __infoB = 20 #ห่อหุ้มกินบ้าน หรือ Encap Encap ดูจากก __?? -> เป็นการกำหนด access_modfier เป็น private

    def __init__(self, infoC, infoD) :
        self.infoC = infoC
        self._infoD = infoD     #Encap ดูจากก __?? -> เป็นการกำหนด access_modfier เป็น private

    # เมื่อใดก๋็จาม encap จะต้องมีเทธอด 2 ตัวนี้้เสมอ คือ get, set ของ data ตัวเป็น
    def setInfoB(self, infoB) : #กำหนด่าให้กับค่า
        self.__infoB = infoB

    def getinfoB(self) : #เอาค่า data ไปใช้
        return self.__infoB
    
    def setInfoD (self, infoD) :
        self.__infoD = infoD

    def getinfoD(self) :
        return self.__infoD
    
    def showInfo(self) :
        print(self.infoA, end="")
        print(self.__infoB, end="")
        print(self.infoC, end="")
        print(self.__infoD)
        print("----------------------------")

ob1 = Dtitest05(30, 40)
ob2 = Dtitest05(30, 100)
ob1.showInfo() # 10 20 30 40
ob1.infoA = 5555
# ob1.__infoB = 999 # ไม่เปลี่ยนเพราะมันถูก encap
ob1.setInfoB(999)
ob1.showInfo() # 555 999 30 40
# print(ob2.__infoB + ob1.__infoD) มันถูก encap ถ้าจะเอาค่าที่เก็บมาใช้งานต้องมาธอด get
print(ob1.getinfoB() + ob1.getinfoD())