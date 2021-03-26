def transfer(ipv4, subnet_mk, arr_num):
    i = 0
    for sector in range(ipv4.split(".")):
        arr_num[i].append(int(sector))
        i += 1

def trans_ntb(arr_num, bits):
    i = 0
    for bit in arr_num:
        bits.append("{0:b}".format(bit))
        i += 1

def main():
    ipv4 = input("please enter the IPv4 address: ")
    subnet_mk = int(input("\nplease enter the subnet mask (only the number): "))

    arr_num = []
    bits = 0

    transfer(ipv4, subnet_mk, arr_num)
    trans_ntb(arr_num, bits)
    print(bits)




if __name__ == '__main__':
    main()