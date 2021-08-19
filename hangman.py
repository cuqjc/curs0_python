import random
import os


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

        secreta = [letra for letra in random.choice(palabra)]
        secreta.pop()
        oculto = ['_' for _ in secreta]

        secreta = normalize(''.join(secreta))
        play(secreta, oculto)


def play(secreta, oculto):
    winner = False
    vidas = '🧡💛💚💙💜🤎🖤💗💖'
    ingreso = ''
    bienvenida = 'Bienveido al juego del ahorcado, tiene que adivinar la palabra antes de agotar las 20 vidas' \
                 ' buena suerte 😎 😎 😎 !!!'
    print(bienvenida)

    oculto = ''.join(oculto)
    # TRASNFORMO LA LISTA x EN UNA VARIABLE PARA QUE SEA MAS LEGIBLE

    while winner is False and vidas > '':
        contador = 0

        print(oculto)
        # MIENTRAS EL USUARIO NO SEA GANADOR Y TENGA VIDAS EJECUTAR

        print('Letras ya ingresadas = ', ingreso)
        # MOSTRAR LETRAS YA INGRESADAS

        letra = input('Ingrese un letra = ')
        # INGRESAR UNA LETRA

        ingreso = str(ingreso) + str(letra) + ' - '
        # GUARDAR LETRA EN UNA VARIABLE PARA QUE EL USUARIO NO LA VUELVA A INGRESAR

        os.system('clear')
        # LIMPIAR PANTALLA

        if letra in secreta:
            print('si esta\nVidas restantes = ', vidas)
            # SI LA LETRA SE ENCUENTRA EN LA PALABRA SECRETA MOSTRAR LAS VIDAS ACTUALES
            oculto = [i for i in oculto]

            for i in secreta:
                # ANALIZAR LETRA POR LETRA DE LA PALABRA SECRETA

                # TRANSFORMAR VARIABLE x EN UNA LISTA PARA PODER BORRAR Y AGREGAR NUEVOS CARACTERES

                if letra == i:
                    oculto.pop(contador)
                    oculto.insert(contador, letra)
                    # SI LA LETRA INGRESADA COINCIDE CON LA LETRA QUE SE ESTA ANALIZANDO EN EL FOR
                    # BORRAR '_' EN EL INDICE EN EL QUE SE ENCUETRA CON X.POP(INDICE)
                    # INSERTAR LETRA INGRESADA EN EL INDICE QUE CORRESPONDE

                    # TRANSFORMAR EL RESULTADO (UNA LISTA) A UNA VARIABLE

                contador += 1
                # AUMENTAR EL CONTADOR QUE REPRESENTA AL INDICE

        else:
            vidas = [i for i in vidas]
            # TRASFORMO LA VARIABLE VIDA A UNA LISTA

            vidas.pop()
            # AHORA QUE ES UNA LISTA PUEDO BORRAR EL ULTIMO ELEMENTO

            vidas = ''.join(vidas)
            # Y VUELVO A TRANSFORMAR LA LISTA EN UNA VARIABLE PARA PODER VERLA MEJOR EN UN PRINT

            print('No esta\nVidas restantes = ', vidas)

        oculto = ''.join(oculto)
        if oculto == secreta:
            winner = True

    if winner:
        print('Felicidades usted gano 👏👏👏👏')

    else:
        print('Fin del juego 🤦‍️🤦‍️🤦‍️😨😭🤮🤡💀 la palabra secreta era = ', secreta)
        print('PERDEDOR VUELVA A INTENTARLO DESPUES ...')


if __name__ == '__main__':
    run()
