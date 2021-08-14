def divisons(num):

    divisors = [i for i in range(1, num + 1) if num % i == 0]
    return divisors


def run():
    num = input('Ingresa un numero = ')
    assert num > '0','El numero es negativo'
    assert num.isnumeric(), 'Debes ingresar un numero'


    # aca hay un error y es que si pongo un numero negativo, este tiene un gion (-)
    # y esto no se considera un numero por la funcion .isnumeric

    # actualizacion... corregi el error, la variable num en un principio es como un str por eso puedo compararla con
    # un numero pero transformado en un str ('0')
    # y no afecta en nada a la funcion .isnumeric porque tambien la compara como si fuera un str por mas que sea un
    # numero
    print(divisons(int(num)))
    print('Termino mi programa')




if __name__ == '__main__':
    run()
