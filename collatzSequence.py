#n/2 if even
#3n+1 if odd
#Biggest sequence for numbers under 1.000.000
#extremadamente ineficiente el ataque a fuerza bruta....
# 837799 es la respuesta, la cadena fue de 524 numeros
#debe haber otra manera de abordarlo... quizas al revés, consuyendo los numeros
#o guadando las candenas ya calculadas para no volver a pasar por ellas

numero = 0
largo_cadena = 0

for i in range(1000000):
    print(i)
    test_numero = i
    test_largo_cadena = 0
    while test_numero > 1:
        #print('ingreso operaciones collatz: {0}'.format(test_numero))
        if test_numero % 2 == 0:
            test_numero = int(test_numero/2)
        else:
            test_numero = 3*test_numero + 1
        test_largo_cadena += 1
        #print('resultado operaciones collatz: {0}'.format(test_numero))
        #input()
    if test_largo_cadena > largo_cadena:
        #print('if final')
        largo_cadena = test_largo_cadena
        numero = i

print(largo_cadena, numero)