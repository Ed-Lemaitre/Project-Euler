from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
from eulermodule import get_primes
from math import sqrt

listaPrimos = get_primes(1000000)
test_number = 0
natural_number = 1

def cantidad_factores(x):
    
    limite = int(sqrt(x)+1)
    factores = dict()

    #print('limite {0} x {1} '.format(limite,x))
    #Lleno un dict() con los pares (fact, exp)
    for i in listaPrimos:
        #print(i)
        factores[str(i)]=0
        if i <= x:
            # print('despues del if  x mod i : {0}'.format(x%i))
            while x%i == 0:
                # print('después del while x:{0} i:{1}'.format(x,i))
                factores[str(i)] += x%i == 0 #sumo 1 si es factor o 0 si no lo es.
                x = x/i
        else:
            break
    
    #calculo la cantidad de factores del numero.
    #Se multiplican entre si los exponentes positivos aumentados en uno.
    respuesta = 1
    for i in factores.values():
        if i > 0:
            respuesta *= (i+1)
    
    return(respuesta)


while True:
    test_number += natural_number
    natural_number += 1

    if cantidad_factores(test_number) > 500:
        print(test_number)
        break