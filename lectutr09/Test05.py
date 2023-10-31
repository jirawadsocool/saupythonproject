# คุณสมบัติเด่น inheritance สือทอด คือ การที่คลาสหนึ่ง สืบทอดอีกคลาสหนึ่ง *** (re-use)
# สืบทอด มีแม่ (super clss/prent) มีลูก (sub class/child)
# แม่มีอะไร ลูกมีด้วย เมื่อมีการสิบทอด (Inherritance)

# คุณสมบัติเล่น polymorphisa (พ้องรูป : พฤิตกรรมเดียวกันแต่วิธีการต่างกัน) คือการที่คลาสลูกเอาเมะอดลาสของแม่มาเขียนใหมา่ที่ลูก

class Sau01 :
    infoA = 10

    def showhi() :
        print('Hi--------')

class Sau02(Sau01) : # Inherritance
    infoB = 20

    def showhey() :
        print('Hey----')

    # overriding method : polymorphism
    def showhi() :
        print('hi hi ih.....')

ob1 = Sau01()
ob2 = Sau02()
ob2.showhi()

