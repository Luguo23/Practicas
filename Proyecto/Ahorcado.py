# Universidad de San Carlos de Guatemala
# Escuela de Ciencias Físicas y Matemáticas
# Programación Matemática 1
# Luis José Velásquez Berdúo
# 20121338

import string

from dibujo_ahorcado import dibujo

# Creo la calse ahorcado, la cual generara el juego
class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.largo = len(palabra)

    def get_palabra(self):
        return self.palabra

    def get_largo(self):
        return self.largo

    # Metodo para obtener el número de vidas por default

    def intentos_default(self):
        intentos = self.get_largo() * 2
        return intentos

    # Metodo para verificar si una letra pertenece a la palabra

    def existe_letra(self, letra):
        return letra in self.get_palabra()

    # Metodo juego por default, donde no se ingresa el número
    # de vidas deseado


    def juego_defualt(self):
        palabra = self.get_palabra()
        vidas = self.intentos_default()
        lista_palabra = []
        for x in palabra:
            if x not in lista_palabra:
                lista_palabra.append(x)

        abecedario = string.ascii_lowercase + "ñ"
        aciertos = []
        intentos = []
        adver = 3

        # El juego termina hasta que adivien todas las letras de la palabra
        # o cuando pierdo todas las vidas

        while len(lista_palabra) > 0 and vidas > 0:
            puntaje = (vidas + adver) * len(aciertos)

            # Muestro el puntaje, la lista de letras usadas y las vidas que quedan
            # un dibujo del ahorcado y la palabra por adivinar en guinones

            print(f"Letras usadas: {' '.join(intentos)} \nTe quedan {vidas} vidas")
            print(f"Tu puntaje es: {puntaje}")

            if vidas > 7:
                print(dibujo[7])
            elif vidas <= 7:
                print(dibujo[vidas])

            palabra_mostrar = [letra if letra in aciertos else '-' for letra in palabra]
            print(f"Palabra: {' '.join(palabra_mostrar)}")

            # Le pido al jugador que escoja una letra y luego verifico si la letra el valida
            # y tambien si pertenece a la palabra por adivinar

            letra_jugador = input("Escoja una letra ").lower()

            print('{:*^80}'.format(""))

            if letra_jugador in abecedario and letra_jugador not in intentos:
                intentos.append(letra_jugador)
                if self.existe_letra(letra_jugador) == True:
                    aciertos.append(letra_jugador)
                    lista_palabra.remove(letra_jugador)
                else:
                    print(f"{letra_jugador} no está en la palabra")
                    print('{:*^80}'.format(""))
                    if adver > 0:
                        adver -= 1
                    else:
                        vidas -= 1

            elif letra_jugador in intentos:
                print(f"La letra {letra_jugador} ya ha sido usada")
                print('{:*^80}'.format(""))
                if adver > 0:
                    adver -= 1
                else:
                    vidas -= 1
            else:
                print("El caracter no es valido")
                print('{:*^80}'.format(""))

        # Muestro mensaje que indican si el juegados gano o perdio el juego

        if vidas == 0:
            print(dibujo[vidas])
            print('{:-^80}'.format("¡¡¡Perdiste!!!"))
            print(f"La palabra era: {palabra}")
        else:
            print(dibujo[7])
            print('{:-^80}'.format("¡¡¡Ganaste!!!"))
            print(f"Adivinaste la palabra: {palabra}")

    # Metodo de juego donde especifico las vidas

    def juego(self, vidas):
        palabra = self.get_palabra()
        lista_palabra = []
        for x in palabra:
            if x not in lista_palabra:
                lista_palabra.append(x)

        abecedario = string.ascii_lowercase + "ñ"
        aciertos = []
        intentos = []
        adver = 3

        while len(lista_palabra) > 0 and vidas > 0:
            puntaje = (vidas + adver) * len(aciertos)

            print(f"Letras usadas: {' '.join(intentos)} \nTe quedan {vidas} vidas")
            print(f"Tu puntaje es: {puntaje}")

            if vidas > 7:
                print(dibujo[7])
            elif vidas <= 7:
                print(dibujo[vidas])

            palabra_mostrar = [letra if letra in aciertos else '-' for letra in palabra]
            print(f"Palabra: {' '.join(palabra_mostrar)}")

            letra_jugador = input("Escoja una letra ").lower()

            print('{:*^80}'.format(""))

            if letra_jugador in abecedario and letra_jugador not in intentos:
                intentos.append(letra_jugador)
                if self.existe_letra(letra_jugador) == True:
                    aciertos.append(letra_jugador)
                    lista_palabra.remove(letra_jugador)
                else:
                    print(f"{letra_jugador} no está en la palabra")
                    print('{:*^80}'.format(""))
                    if adver > 0:
                        adver -= 1
                    else:
                        vidas -= 1

            elif letra_jugador in intentos:
                print(f"La letra {letra_jugador} ya ha sido usada")
                print('{:*^80}'.format(""))
                if adver > 0:
                    adver -= 1
                else:
                    vidas -= 1
            else:
                print("El caracter no es valido")
                print('{:*^80}'.format(""))

        if vidas == 0:
            print(dibujo[vidas])
            print('{:-^80}'.format("¡¡¡Perdiste!!!"))
            print(f"La palabra era: {palabra}")
        else:
            print(dibujo[7])
            print('{:-^80}'.format("¡¡¡Ganaste!!!"))
            print(f"Adivinaste la palabra: {palabra}")

