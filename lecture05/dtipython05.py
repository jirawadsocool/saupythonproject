#คำนวณเงินที่จะแชร์กัน ป้อนเงิน ป้อนคน แล้วคำนวณและแสดงเงินที่จะแชร์กันทางหน้าจอ
#โดยหใ้เขียนเป็นฟังก์ชัน ขอ 2 ฟังก์ชัน
#cast/converstion

#รับข้อมูล
def inputMoneyPerson ( ) :
    monney = float(input('ป้อนเงิน : '))
    person = int(input('ป้อนคน : '))
    return monney, person

#คำนวณ แล้วแสดงผลออกมา
def calAndShowMoneyShare(money, person) : 
    #เงิน ขอทศนิยม 2 ตำแหน่ง แชร์กันขอเเป็นเลยจำนวเต็มปัดขึ้น
    print(f'จำนวนเงิน {money:.2f} บาท คน {person} คน แชร์กันคนละ {round(money/person)} บาท ')
    print("จำนวนเงิน", "%.2f" % money ,"บาท คน", person ,"คน แชร์กันคนละ", round(money/person),"บาท" )
    print("จำนวนเงิน" +" "+ str("%.2f" % money) +" "+ "บาท คน" +" "+ str(person) +" "+ "คน แชร์กันคนละ" +" "+ str(round(money/person)) +" "+"บาท")
    print("จำนวนเงิน {} บาท คน {} คน แชร์กันคนละ {} บาท" .format("%.2f"%money,person,round(money/person)))
    print("จำนวนเงิน %s บาท คน %s คน แชร์กันคนละ %s บาท" %("%.2f"%money,person,round(money/person)))



money, person = inputMoneyPerson( )

calAndShowMoneyShare( money, person )