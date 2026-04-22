for x in range (4):
    for y in range (5):
        if (y == 2):
            print ("0", end= " ")
        else:
            print ("x", end= " ")
    print()
print("")

for i in range (4):
    for j in range (5):
        if ( i == 0 or i == 3) and (j == 2):
            print ("0", end= " ")
        elif (i == 1 or i == 2) and (1<=j<=3):
            print("0", end= " ")
        else:
            print ("x", end= " ")
    print()