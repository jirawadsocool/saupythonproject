# Destructor

from collections.abc import Iterable


class DtiTest04 :
    data1 = 30
    # comstrutor
    def __init__(self, data2) :
        self.data2 = data2
        print('Hi....')

    def dotask1(self) :
        print("^.^")

    def doTask2(value) :
        print(value)

    # Destructor
    def __dir__(self) :
        print('Bye bye////')

# ------------------------------------
sauA =DtiTest04(20)
sauB =DtiTest04(30)
sauC =DtiTest04(20)

sauC.doTask2('T_T')
sauC.dotask1()
print(sauA.data1 + sauB.data1)