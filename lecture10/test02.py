# เขียนข้อมูลลองไฟล์
# เปิดไฟล์เพื่อเรียกข้อมูลไฟล์
f_dit = open('myfile01.txt', 'w', encoding='utf-8')

f_dit.write('hello')
f_dit.write('Hi.....\n')
f_dit.write('สวัสดีครับทุกคนว่่าไงวัยรุ่น......\n')

f_dit.close()

print('บันทึกข้อมูลลงไฟล์เรียบร้อยแล้ว......')