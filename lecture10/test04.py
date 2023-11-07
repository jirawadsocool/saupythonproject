# เขียนข้อมูลลองไฟล์
# เปิดไฟล์เพื่อเรียกข้อมูลไฟล์
f_dit = open('myfile03.txt', 'a', encoding='utf-8')

f_dit.write('AAAA\n')
f_dit.write('BBBB\n')

f_dit.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว......')