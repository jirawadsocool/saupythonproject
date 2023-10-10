#variabla
score = 5464
stu_name = "สมชาย"
falg = True
#----------------------
#Lisy 
                                   # 0 1                 
    #   0    1     2      3         4           5
varl = [10, 20, 'Hello', True, [111, 'Wow'], 'มานะ']
    #   -6   -5    -4     -3        -2          -1
                                    # -2 -1

print(varl[0] + varl[1])
print(varl[-6] + varl[-5])
print(varl[0] + varl[4][0])
print(varl[-6] + varl[-2][-2])

# tuple
                                # 0    1 
    #    0   1     2       3       4          5
var2 = (10, 20, 'hello', True (111, 'Wow'),'มานะ')
    #    -6   -5   -4      -3      -2          -1
print(var2[0] + var2[1])
print(var2[-6] + var2[-5])
print(var2[-6] + var2[-2][-2])
print(f'{var2[2]}........{var2[5]} {var2[4][1]}.....') # Hello..........มานะ.............. Wow....