#Function 1 : no parameter/no return
def funcA( ) :
    print('AAA')
    print('BBB')
    #funcB( ) ไม่ควรเรียกฟังก์ชั้นกันไปมา
    #ไม่มีคำสั่ง return

def funcB( ) :
    print(111)
    funcA( )

funcA( )
funcA( )
funcB( )
funcA( )