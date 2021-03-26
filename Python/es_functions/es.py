#argomenti/parametri di defoalt in input alle funzioni

def fun(lista_numeri = [10, 11], stampa = False):
    lista_quadrati = [x*x for x in lista_numeri]
    if stampa:
        print(lista_quadrati)
    return lista_quadrati

fun(stampa = True, lista_numeri = [4, 5])