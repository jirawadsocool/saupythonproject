# อ่่านข้อมูลจากไฟล์
f_dit = open('myfile01.txt', 'r', encoding='utf-8')

try :
    data = f_dit.readline()
    print(data, end='')
    data = f_dit.readline()
    print(data, end='')
    data = f_dit.readline()
    print(data, end='')
except Exception :
    print('ติดต่อ Admin 0803232....')
finally :
    f_dit.close()