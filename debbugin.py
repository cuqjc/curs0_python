def divisons(num):
    try:
        if num < 1:
            raise ValueError('Debe ingresar un numero positivo ...')

        else:
            divisors = [i for i in range (1, num + 1) if i % 2 == 0]


    except ValueError as ve:
        print('mal ahi')
        divisors = ve
    return divisors


def run():
    try:
        num = int(input('Ingresa un numero = '))
        print(divisons(num))
        print('Termino mi programa')

    except ValueError:
        print("Debes ingresar solo numeros ....")


if __name__ == '__main__':
    run()
