#push e pop della pila per comodità messe in delle funzioni

def push_(pila,elemento):
    pila.append(elemento)


def pop_(pila):
    return pila.pop()

# questa funzione crea una seconda pila composta da soltanto le parentesi e controllerà se ci sono tutte

def control(stack):
    stack_par = []
    no_dif = True
    for index in stack:
        if is_par(index):
            push_(stack_par, index)
    while no_dif:
        #non so come fare il controllo per vedere se ci sono effettivamente tutte le parentesi
        #se ci sono errori ci sarà un
        #return False

    return True

#controlla se il carattere scelto è una parentesi grazie al codice achii

def is_par(let):
    index = int(let)
    if int(index) == 40 or int(index) == 40 or int(index) == 91 or int(index) == 93 or int(index) == 123 or int(index) == 125:
        return True
    return False

#nel main viene messa in uno stack a se ogni lettera di una stringa uscendo solo quando viene premuto a capo

def main():
    stack = [];
    acapo = False;
    print("input the string")
    while not acapo:
        let = input("", end = '')
        if let != '\n':
            push_(stack, let)
        else:
            acapo = True

    all_of_them = control(stack)

    #dopo il controllo si stabilisce se ci sono errori o no

    if all_of_them:
        print("no errors on the brackets")
    else:
        print("there is an error")

if __name__ =="__main__":
    main()