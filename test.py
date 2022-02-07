from multiprocessing import cpu_count


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

def mcd_two_inputs_max_min(a,b):
    resto = a % b
    # print(a,b,resto)
    while resto != 0:
        a, b = max(b, resto), min(b, resto)
        # print(a,b)
        resto = a % b
    return(b)




def counter(fn):
	counter = 0

	def inner(*args, **kwargs):
		nonlocal counter
		counter += 1
        print(counter)
		return fn(*args, **kwargs)
    return inner

def add(a,b):
    return a + b

add = counter(add)

print(add(1,2))