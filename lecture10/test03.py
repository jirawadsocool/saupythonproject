# เขียนข้อมูลลองไฟล์
# เปิดไฟล์เพื่อเรียกข้อมูลไฟล์
f_dit = open('myfile02.txt', 'w', encoding='utf-8')

f_dit.write('SAU')
f_dit.write('DTI.....\n')
f_dit.write('มาเด้อลาบแซ๋บๆ......\n')

f_dit.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว......')