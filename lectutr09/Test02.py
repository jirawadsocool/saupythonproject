class DTITest03 :
    # data
    infoA = 10

    # construter จะเป็นตัวทำให้ object ที่สร้างจากคลาสเดียวกันไม่จำเป็นต้องเหมือนกัน
    # constuter จะทำงานทุกครั้งที่มีการสร้าง object
    def __init__(self, infoB, infoC):
        self.infoB = infoB
        self.infoC = infoC

    # method
    def showmixandinfo(self, mix) :
        print(self.infoA + self.infoB + self.infoC + mix)

# สร้าง object
sau1 = DTITest03(20, 30)
sau2 = DTITest03(10, 100)
sau3 = DTITest03(20, 30)