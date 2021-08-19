palabra = 'manzana'
x = '*' * len(palabra)

letra = 'z'
op = input('Ingrese su letra = ')
contador = 1
for a in palabra:
    print(a)
    if a == op:
        for i in x:
            a.replace(a, op)

print(x)
print(palabra)