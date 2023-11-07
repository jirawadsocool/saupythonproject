# อ่่านข้อมูลจากไฟล์
f_dit = open('myfile01.txt', 'r', encoding='utf-8')

try :
    data = f_dit.read()
    
    print(data)
except Exception :
    print('ติดต่อ Admin 0803232....')
finally :
    f_dit.close()