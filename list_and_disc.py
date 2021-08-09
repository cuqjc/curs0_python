def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dict = {'fristname': 'Facundo', 'lastname': 'Garcia'}

    super_list = [
        {'fristname': 'Facundo', 'lastname': 'Garcia'},
        {'fristname': 'Miguel', 'lastname': 'Torres'},
        {'fristname': 'Pepe', 'lastname': 'Rodelo'},
        {'fristname': 'Susana', 'lastname': 'Martinez'},
        {'fristname': 'Jose', 'lastname': 'Garcia'},
        # LISTA QUE CONTINE CINCO DICCIONARION....
    ]
    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integral_nums': [-1, -2, 0, 1, 2],
        'floating_nums': [1.1, 4.5, 6.43]
    }  # DICCIONARIO QUE CONTIENE TRES LISTAS....

    for key, value in super_dict.items():
        print(key, '-', value) # ESTE NUMERO NOS VA A MOSTRAR LAS
        # TRES LISTAS QUE TENEMOS EN NUESTRO DICCIOANRIO

    for i in super_list:
        print(i['fristname'], i['lastname'])
        # CON ESTE FOR PODEMOS VER EL LOS VALORES LLAMANDO A LAS LLAVES DE LOS DICCIONARIOS DENTRO DE LA LISTA

        # ESTE FOR NOS PERMITE RECORRER LAS LLAVES Y VALORES AL MISMO
        # TIEMPO DE UN DICCIONARIO EN UN CICLO


if __name__ == '__main__':
    run()
