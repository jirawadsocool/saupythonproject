# ลบไฟล์
import os
from os import remove

if os.path.exists('myfile02.txt') :
    # os.remove('myfile01.txt')
    remove('myfile02.txt')
    print('ลบไฟล์เรียบร้อยแล้ว')
else :
    print('ไม่มีไฟล์ที่จะลบ')