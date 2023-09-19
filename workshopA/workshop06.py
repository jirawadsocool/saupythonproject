def main() :
    name = input("ชื่อผู้กู้ : ")
    amount = float(input("ยอดเงินกู้ : "))
    if amount >= 1000:
        interest = 0.025
    else :
        interest = 0.055