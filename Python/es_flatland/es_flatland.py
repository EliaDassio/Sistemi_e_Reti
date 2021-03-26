import csv
import random

position_dictionary = {}

def nord(x, y):
    y = y + 10

def south(x, y):
    y = y - 10

def est(x, y):
    x = x + 10

def west(x, y):
    x = x - 10

dictionair_directions = {0:nord, 1:south, 2:est, 3:west}

def make_position_dictionair(position_dictionary):

    x = 0
    y = 0

    for index in range(60):
        func = random.randint(0, 3)
        dictionair_directions[func](x,y)
        position = [x, y]
        position_dictionary[index] = position

    print(position_dictionary)



def main():

    make_position_dictionair(position_dictionary)

    with  open('file.csv', 'w') as csvfile:

        csvwriter = csv.writer(csvfile)

        for key, value in position_dictionary.items():
            lista = [key, value[0], value[1]]
            csvwriter.writerow(lista)

if __name__ =="__main__":
    main()