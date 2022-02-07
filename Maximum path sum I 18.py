# Maximum path sum I 18.py
triangle = open('triangle.txt', 'r')

triangle_lst = []

for line in triangle:
    triangle_lst.append(line.replace('\n','').split())

sum = 0 # Lleva el registro de la maxima suma


# for a in triangle_lst[len(triangle_lst)-1]:
#     pass

altura_triangulo = len(triangle_lst)

for i in range(0,altura_triangulo):
    print (altura_triangulo - i - 1)