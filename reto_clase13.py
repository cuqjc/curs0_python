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
    all_platzi_workers = list(filter(lambda devs:  devs['organization'] == 'Platzi' ,DATA))
    all_platzi_workers = list(map(lambda devs:  devs['name'] ,all_platzi_workers))

    print('\nNombre de las personas que trabajan en Platzi =')
    for devs in all_platzi_workers:
        print('\t\t',devs)

    all_python_devs = list(filter(lambda devs: devs['language'] == 'python', DATA))
    all_python_devs = list(map(lambda devs: devs['name'], all_python_devs))

    # ESTO ES MAS COMPLICADO TAL VEZ con lambda agarro el lenguaje que tengo en devs['language'] (que saque del
    # parametro DATA ) y lo comparo con el lenguaje 'python', si es true se filta y se guarda en la lista
    # peeero es no es toodo, eso va a guardarme la llave que contengan todos los datos de este trabajador
    # para volver a filtarlo uso la funcion map y agrego el valor de  devs['name'] a la misma funcion all_python_devs


    print('\nPersonas que usan python =')

    for devs in all_python_devs:
        print('\t\t',devs)

    old_people = [workers['name'] for workers in DATA if workers['age'] > 70]
    # ACA HAY QUE USAR MUCHO LA LOGICA, pensar bien y simple >> para workes['name'] (workers es una variable temporal
    # que no afencta en nada a lo de afuera, solo sirve como un lugar para guardar el valor de 'name')
    # es como decir >> guarda el nombre de cada workers (for) que esta en DATA si (if) la edad de ese trabajador
    # (workers[age'] es mayor a 70)

    print('\nLa gente mas vieja =')
    for older in old_people:
        print('\t\t', older)

    adults = [workers['name'] for workers in DATA if workers['age'] > 18 ]
    print('\nGente mayor a 18 años =')
    for adult in adults:
        print('\t\t', adult)



if __name__ == '__main__':
    run()