for i in range(3) :
    รหัสนักเรียน = input("กรอกรหัสนักเรียน : ")
    ชือนักเรียน = input("กรอกชื่อนักเรียน : ")
    scores = input(int('กรอกคะแนน : '))
    for j in range (3) :
        scores = float(input(f"กรอกคะแนนครั้งทีี่ {j+1}:"))
        scores.append(scores)
    คำนวณคะแนน = sum(scores) / len(scores)
    students.append((รหัสนักเรียน, ชือนักเรียน , คํานวณคะแนน))
print("จะได้")
for student in students:
    รหัสนักเรียน, ชือนักเรียน , คํานวณคะแนน = student
    print(f"รหัสนักเรียน : {รหัสนักเรียน}, ชื่อนักเรียน : {ชือนักเรียน}, คะแนนเฉลี่ย : {คํานวณคะแนน:.2%f}")                                                                           