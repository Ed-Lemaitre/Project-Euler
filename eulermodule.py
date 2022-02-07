#Entrega una lista de primos menores o iguales al argumento n
from operator import is_


def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

#Verifica si una cadena es palíndrome.
def is_palindrome(cadena):
    """ recibe un str()"""
    flag = True
    largo = int(len(cadena)/2)

    for i in range(largo):
        if not(cadena[i] == cadena[len(cadena)-1-i]):
            flag = False
            break
    return flag

# Entrega el mcd de una lista entregada, funciona en conjunto con
# mcd_two_inputs_max_min
def mcd_lista(lista):
    lista_sorted = sorted(lista, reverse=True)
    respuesta = mcd_two_inputs_max_min(lista_sorted[0], lista_sorted[1])
    # print(respuesta)
    for i in range(2,len(lista_sorted)):
        # print('entre')
        a, b = max(respuesta,lista_sorted[i]), min(respuesta,lista_sorted[i])
        # print(a,b)
        respuesta = mcd_two_inputs_max_min(a,b)
    return(respuesta)


# Los argumentos a esta funcion deben entregarse en orden (max, min)
def mcd_two_inputs_max_min(a,b):
    resto = a % b
    # print(a,b,resto)
    while resto != 0:
        a, b = max(b, resto), min(b, resto)
        # print(a,b)
        resto = a % b
    return(b)