#คำสั่ง break กับ continue ที่มักจะใช้ร่วมกับ control flow
for x in range(5) : 
    if x == 3 :
        break # ทำงานเมื่อไหร่จบ Loop ทันที
    print(f'SAI....{x}')

print('+++++++++++++++++++++++++++++++++++')

for y in range(5) : 
    if y == 3 :
        continue;   # continue ทำงานเมื่อไหร่จบรอบนั้น ไปรอบต่อไปทันที
    print(f'DTI.....{y}')