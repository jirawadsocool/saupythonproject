# OOP
class DtiSau :
    # data/preoperty member ค่าข้อมูล
    stu_name = 0
    score = 0
    gpa = 0

    # memthod member คือการทำงาน
    def histudent(self) :
        print(f'สวัสดี {self.stu_name}')

    def showscoreandgrade(self):
        print(f'คะแนน{self.score} ได้เกรด {self.gpa}')
    
# สร้าง object
obj01 = DtiSau() # ชื่อคลาสที่มีวงเล็บเราเรียกว่า เป็นการสั่งให้
obj02 = DtiSau()

obj01.stu_name = 'สมชาย'
obj01.histudent()
obj02.stu_name = 'สมหญิง'
obj02.score = 10
obj02.gpa = 3.99