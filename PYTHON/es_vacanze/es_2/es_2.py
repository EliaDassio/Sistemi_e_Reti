import random

def genera_mac():
    for i in range(6):
        des = random.randint(0, 3)
        if des == 1:
            val_1 = random.randint(48, 57)
        else:
            val_1 = random.randint(65, 70)
        des = random.randint(0, 3)
        if des == 1:
            val_2 = random.randint(48, 57)
        else:
            val_2 = random.randint(65, 70)
        if i < 6:
            print(chr(val_1) + chr(val_2) + ":", end = '')
        else:
            print(chr(val_1) + chr(val_2))
    print("\n")


ready = input("generate a mac address ?(press enter): ")
genera_mac()