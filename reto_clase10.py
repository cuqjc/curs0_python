def run():
    x = 0
    for i in range(1,101):
        number = {i: i ** 3}
        print(number)

    diccionario = {i for i in range(1, 101)}
    print(diccionario)


if __name__ == '__main__':
    run()