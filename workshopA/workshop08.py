def main () :
    จังหวัด = input("จังหวัด : ")
    ph = float(input("กรอกค่า PH : "))
    if 7 <= ph <= 8:
        print("Result is Normal")
    elif ph > 8 :
        print ("Result is Acid")
    else:
        print("Result is Alkali")
        if __name__ == "__main__" :
            main()