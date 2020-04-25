from my_pkg.convert import convert
from my_pkg.uaii import UAI



while(True):
    menu = int(input("Select menu: 1) conversion 2) union/intersection 3) exit? "))

    if menu == 1:
        BinNum = input("input binary number : ")
        convert(BinNum)

    elif menu == 2:
        L1 = input("1st list: ")
        L2 = input("2nd list: ")
        UAI(L1, L2)

    elif menu == 3:
        exit(0)

