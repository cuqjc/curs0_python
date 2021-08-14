#def saludo(func):
#    func()

#def hola():
#    print('Hola')


#def adios():
#    print('Adios')


#saludo(hola)
#saludo(adios)



#my_list = [2, 2, 2, 2, 2]

#odd = list(map(lambda x: x**2, my_list))

#print(odd)

from functools import reduce
my_list = [2, 2, 2, 2, 2]

odd = reduce(lambda a, b: a * b, my_list)

print(odd)