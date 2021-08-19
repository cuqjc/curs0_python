import os


def read():
    # leer archivo que contiene los numeros del 1 al 10 y convertir cada linea en una lista
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
    input()
    os.system('clear')


def write():
    names = ['Facundo', 'Miguel', 'Pepe', 'Christian ', 'Rocio']
    with open('./archivos/names.txt', 'w', encoding='utf_8') as f:
        for name in names:
            f.write(name)
            f.write('\n')



def run():
    read()
    write()



if __name__ == '__main__':
    run()