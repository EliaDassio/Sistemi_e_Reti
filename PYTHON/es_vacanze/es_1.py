import random

def randomize(index):
    for i in range(index):
        des = random.randint(1, 3)
        if des == 1:
            val = random.randint(48, 57)
        elif des == 2:
            val = random.randint(65, 90)
        else:
            val = random.randint(97, 122)
        print(chr(val), end = '')
    print("")


witch = int(input("short or long pasword? (1 for short or 2 for long)? "))

while witch != 1 and witch != 2:
    witch = int(input("please answer correctly, short or long pasword (1 for short or 2 for long)? "))

print("")

if witch == 1:
    index = 8
if witch == 2:
    index = 20

randomize(index)
