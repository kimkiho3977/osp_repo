import operator

def convert(data):
    Bin = data

    DEC = int(Bin,2)

    OCT = format(DEC, 'o')
    HEX = format(DEC, 'x')

    print("OCT> %s" %OCT)
    print("DEC> %d" %DEC)
    print("HEX> %s" %HEX.upper())


if __name__ == "__main__":

    BinNum = input("input binary number : ")
    convert(BinNum)