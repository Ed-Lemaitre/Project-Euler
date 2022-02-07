def contador(func):
    cont = 0
    def interior(*args,**kwargs):
        nonlocal cont
        cont += 1
        return func(*args,**kwargs), cont
    return interior

def add(a,b):
    return(a+b)

add = contador(add)

for i in range(3):
    print(add(1,2))