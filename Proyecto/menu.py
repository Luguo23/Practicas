# Universidad de San Carlos de Guatemala
# Escuela de Ciencias Físicas y Matemáticas
# Programación Matemática 1
# Luis José Velásquez Berdúo
# 20121338

import random
import string

from Ahorcado import Ahorcado

# Funcion que busca de manera aleatoria una palabra en el texto para jugar al ahorcado

def palabra(archivo):
    signos = string.punctuation
    numeros = string.digits
    text = ''
    with open(archivo, 'r') as file:
        for linea in file:
            nueva_linea = linea.replace("\n", " ")
            text = text + nueva_linea
    lista = text.split()

    palabra = random.choice(lista).strip(signos).strip(numeros).lower()
    while len(palabra) < 3:
        palabra = random.choice(lista).strip(signos).strip(numeros).lower()

    return palabra

# Menú y ejecucion del juego

otravez = "s"
while otravez == "s":
    print('{:-^80}'.format(""))
    print('{:^80}'.format("Juego del ahorcado: adivina la palabra"))
    print('{:-^80}'.format(""))

    print('{:^80}'.format("1 Jugar      2 Cambiar número de vidas"))

    op = input("Elija una opción: ")

    if op == "1":
        plb = palabra("texto.txt")
        juego = Ahorcado(plb)
        juego.juego_defualt()
        otravez = input("¿Desea jugar de nuevo? s/n: ")
    elif op == "2":
        vidas = int(input("Escoja el número de vidas: "))
        plb = palabra("texto.txt")
        juego = Ahorcado(plb)
        juego.juego(vidas)
        otravez = input("¿Desea jugar de nuevo? s/n: ")
    else:
        print("Error: opcion no valida")


print('{:-^80}'.format("Fin del programa"))