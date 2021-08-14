

DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def run():


    all_python_dev = [worker['name'] for worker in DATA if worker['language'] == 'python']
    # con el for voy a recorrer cada indice de la lista DATA
    # Y si la llave language es igual a python entonces, guardo la llave nombre en worker
    # Compara el valor de la llave language
    # Guarda el valor de la llave name en all_python_dev en el indice correspondiente

    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']

    # esto hace lo mismo que la lista de arriba pero con la organizacion a la que pertenecen

    old_people = list(map(lambda worker: worker | {'old': worker['age']> 70 },DATA))

    # Con esto creamos la lista old_people con los datos de DATA, agregamos una llave (old), y con
    # esto sabemos si es TRUE o FALSE >> worker['age']> 70 y lo guardamos en el valor worker y luego a la lista

    for worker in all_python_dev:
        print('Python dev :', worker)



    for worker in all_platzi_workers:
        print('Workers of python :', worker)

    for worker in old_people:
        print('Viejos :', worker)

    old = list(filter(lambda adult: adult['age'] > 17,DATA))
    old = list(map(lambda adult: adult['name'], old)) # Esto analisa nuevamente la lista old anterior y guarda
    # solo los nombres

    # Paso el parametro DATA y analiso uno por uno  los datos
    # Con la funcion lambda asigno cada valor de DATA a .adult y extraigo 'age' para comparar si es mayor a 17
    # Filtro y guardo los que den true en lambda, pero esto me va a guardar toodos los datos de los diccionarios
    # Si paso por el filtro entonces nos va a mostrar todas las personas que sean mayores a 17

    for x in old:
        print(x) # Esto solo muestra los nombres de las personas que son mayores a 17 per el print de abajo muestra
        # el nombre y la edad

        #print(x['name'], x['age']) # Podemos poner asi para que nos muestre el valor de la llave name y el valor de
        # de la llave age, osea nombre y edad , esto se puede hacer de otra mejor forma como por ejemplo volver
        # a listar toodo pero con la funcion de orden superior MAP




if __name__ == '__main__':
    run()