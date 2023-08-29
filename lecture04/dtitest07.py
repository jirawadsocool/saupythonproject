emd_id = input("ป้อนรหัสพนังงาน : ")
emd_name = input('ชื่อพนังงาน : ')
emp_salary = float(input("เงินเดือนพนังงาน : "))
minus_tax = emp_salary - (emp_salary * 7 / 100) - 500
minus_tax_lowerfloat = "%.2f" % minus_tax

print(f"ID {emd_id} คุณ {emd_name} เงินเดือนของพนังงาน {emp_salary} เงินเดือนสุทธิ {minus_tax}")
