import random

def randomize_simple():
    for i in range(8):
        des = random.randint(1, 3)
        if des == 1:
            val = random.randint(48, 57)
        elif des == 2:
            val = random.randint(65, 90)
        else:
            val = random.randint(97, 122)
        print(chr(val), end='')
    print("\n")

def randomize_complex():
        for i in range(20):
            val = random.randint(1, 255)
            print(chr(val), end='')
        print("\n")

witch = int(input("short or long pasword? (1 for shart or 2 for long)? "))

while witch != 1 and witch != 2:
    witch = int(input("please answer correctly, short orlong pasword (1 for shart or 2 for long)? "))

print("\n")

if witch == 1:
    randomize_simple()
if witch == 2:
    randomize_complex()