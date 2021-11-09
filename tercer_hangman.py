import random


def normalize(s):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def run():
    with open('./hangman/data.txt', 'r', encoding='utf-8') as data:
        palabra = [line for line in data]

        cadena = [letra for letra in random.choice(palabra)]
        cadena.pop()
        cadena = normalize(''.join(cadena))

    print(cadena)
    indice_allado = 0
    winner = False
    secreta = '-' * len(cadena)
    while not winner:
        letra = input("Ingrese una letra de la palabra secreta = ")
        print('\n' * 30)

        if letra in cadena and len(letra) == 1:

            for i in range(cadena.count(letra)):  # RANGO = CANTIDAD DE VECES QUE APARECE LA LETRA EN LA PALABRA
                reemplazar_index = cadena.find(letra, indice_allado)  # BUSCAR INDICE DONDE SE ENCUETNRA LA LETRA

                secreta = secreta[:reemplazar_index] + letra + secreta[reemplazar_index + 1:]
                # SEPARAMOS LA CADENA ANTES DE LA LETRA Y LA REEMPLAZAMOS PARA LUEGO UNIRLA AL RESTO DE LA CADENA

                indice_allado = reemplazar_index + 1  # SUMAMOS EL INDICE PARA BUSCAR LETRAS IGUALES POR ENCIMA DE ESTA

            indice_allado = 0
            if secreta == cadena:
                print("Felicidades encontro la palabra ")
                winner = True
        else:
            print('Incorrecto ingrese otra letra...')

        print('Secreta = ', secreta)


run()
