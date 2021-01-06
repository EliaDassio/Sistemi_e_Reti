def min_max():
    print("\n")
    year_1 = input("input the first year: ")
    print("\n")
    year_2 = input("input the second year: ")

    minn = 10000.0
    maxx = 0.0

    if year_1 > year_2:
        dist = int(year_1) - int(year_2)
        par = int(year_2)
    else:
        dist = int(year_2) - int(year_1)
        par = int(year_1)

    for index in range(dist):
        i = par + index
        if year_val[str(i)] < minn:
            minn = year_val[str(i)]
        if year_val[str(i)] > maxx:
            maxx = year_val[str(i)]

    print("\n\n")
    print("the minimum variation between " + year_1 + " and " + year_2 + " is " + str(minn))
    print("\n\n")
    print("the maximum variation between " + year_1 + " and " + year_2 + " is " + str(maxx))
    print("\n\n")



year_val = {}
div = 1
summ = 0.0
p_key = '2016'
key = '2016'
first_line = 0
file = open("annual.csv", "r")
if file.readable():
    for line in file.readlines():
        if first_line > 0:
            cont = 0;
            for index in line.split(','):
                if cont == 1:
                    key = index
                    if key != p_key:
                        year_val[p_key] = summ / div
                        div = 0
                        summ = 0
                        year_val[key] = 0
                elif cont == 2:
                    div += 1
                    summ += float(index)
                    cont = 0
                p_key = key
                cont += 1
        first_line += 1
    min_max()
else:
    print("can't omen the file")
file.close()