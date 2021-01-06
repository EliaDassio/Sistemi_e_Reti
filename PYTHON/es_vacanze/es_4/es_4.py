def encode ():
    word = input("input the word to decode: ")
    print("\n")
    for letter in word:
        letter = ord(letter) + 15
        if (letter > 90 and letter < 97) or letter > 122:
            letter = letter - 26
        print(chr(letter), end = '')
    print("\n\n")

def decode ():
    word = input("input the word to decode: ")
    print("\n")
    for letter in word:
        letter = ord(letter) - 15
        if letter < 65 or (letter < 97 and letter > 90):
            letter = letter + 26
        print(chr(letter), end = '')
    print("\n\n")

witch = int(input("do you want to encode or decode? (1 for encode or 2 for decode)? "))

while witch != 1 and witch != 2:
    witch = int(input("please answer correctly, do you want to encode or decode? (1 for encode or 2 for decode)? "))

print("\n")

if witch == 1:
    encode()
if witch == 2:
    decode()