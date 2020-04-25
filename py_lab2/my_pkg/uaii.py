import operator

def UAI(L1, L2):
    list1_str = L1
    list2_str = L2

    list1_str = list1_str.replace("[", "")
    list1_str = list1_str.replace(" ", "")
    list1_str = list1_str.replace("]", "")

    list2_str = list2_str.replace("[", "")
    list2_str = list2_str.replace(" ", "")
    list2_str = list2_str.replace("]", "")

    list1 = list()
    list2 = list()

    list1 = list1_str.split(',')
    list2 = list2_str.split(',')

    list1 = set(list1)
    list2 = set(list2)

    uni = list1 | list2
    intersec = list1 & list2

    print("Union: ", end='')
    print(sorted(uni))
    print("Intersection: ", end='')
    print(sorted(intersec))

if __name__ == "__main__":

    L1 = input("1st list: ")
    L2 = input("2nd list: ")
    UAI(L1, L2)