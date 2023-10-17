class Test04 :
    date1 = 10

    # constritar
    def __inti__(self, date2, date3):
        print('Hi.....')
        self.date1 = date2
        self.date3 = date3

    # memthod member
    def shiwsumdate(self):
        print(self.date1 + self.date2 + self.date3)
        self.ShowWow()

    def ShowWow(self):
        print('Wow wow wow')

objA = Test04(20, 30)
objB = Test04(10, 20)
objC = Test04(20, 100)
objD = Test04(20, 30)