'''
Universidad de San Carlos de Guatemala
Escuela de Ciencias Físicas y Matemáticas
Programación Matemática 1 primer semestre 2023
Practica 2
Luis José Velásquez Berdúo 2012 13358
Este Programa Resuelve el juego de la Torre de Hanoi y simula la solución
'''

import time
# funciones
# Funcion que mueve los discos
def mover_dic(cadena):
    pass
    init = cadena[1]
    final = cadena[2]
    if init == "A":
        j = 0
        k = len(A) - 1
        p = False
        while not p:
            if '*' in A[j]:
                temp = A[j]
                if final == "B":
                    if '|' in B[k]:
                        A[j] = B[k]
                        B[k] = temp
                        p = True
                    else:
                        k = k - 1
                if final == "C":
                    if '|' in C[k]:
                        A[j] = C[k]
                        C[k] = temp
                        p = True
                    else:
                        k = k - 1
            else:
                j = j + 1

    if init == "B":
        j = 0
        k = len(B) - 1
        p = False
        while not p:
            if '*' in B[j]:
                temp = B[j]
                if final == "A":
                    if '|' in A[k]:
                        B[j] = A[k]
                        A[k] = temp
                        p = True
                    else:
                        k = k - 1
                if final == "C":
                    if '|' in C[k]:
                        B[j] = C[k]
                        C[k] = temp
                        p = True
                    else:
                        k = k - 1
            else:
                j = j + 1

    if init == "C":
        j = 0
        k = len(C) - 1
        p = False
        while not p:
            if '*' in C[j]:
                temp = C[j]
                if final == "B":
                    if '|' in B[k]:
                        C[j] = B[k]
                        B[k] = temp
                        p = True
                    else:
                        k = k - 1
                if final == "A":
                    if '|' in A[k]:
                        C[j] = A[k]
                        A[k] = temp
                        p = True
                    else:
                        k = k - 1
            else:
                j = j + 1

# Función que resuelve Hanoi
def hanoi(m, inc, fnl, piv):
    if m == 1:
        mov.append(str(m)+inc+fnl)
    else:
        hanoi(m-1, inc, piv, fnl)
        mov.append(str(m)+inc+fnl)
        hanoi(m-1, piv, fnl, inc)

# Funcion Menu

# Funcion que existe un numero en la cadena
def es_numero(n):
    numero = "0123456789"
    for x in numero:
        if x in n:
            return True

def menu():
    print('{:-^80}'.format("Torre de Hanoi"))
    r = False
    while not r:
        n = input("Ingrese el número de discos: ")
        if n == '':
            n = 3
            print("El número de discos por defecto es:", n)
            confirmacion = input("¿Esta de acuerdo? s/n: ")
            if confirmacion == "s":
                r = True
        elif es_numero(n) != True:
            print("Error: Ingrese un número entero entre 3 y 10")
        else:
            if 2 < int(n) < 11:
                print("El número de discos es: ", n)
                confirmacion = input("¿Está de acuerdo? s / n: ")
                if confirmacion == "s":
                    r = True
            else:
                print("Fuera de limite: ingrese un número entero entre 3 y 10")
    q = False
    while not q:
        t = input("Ingrese el tiempo entre movimientos: ")
        if es_numero(t) != True:
            print("Error: Ingrese un número entero entre 1 y 10")
        else:
            if 0 < int(t) < 11:
                q = True
            else:
                print("Fuera de limite: ingrese un número entero entre 1 y 10")

    v = False
    while not v:
        simul = input("¿Desea simular la solución? s/n: ")
        if simul == "s" or simul == "n":
            v = True
        else:
            print("Ingrese \"s\" para sí o \"n\" para no")
    parametros = [n, t, simul]
    return parametros

otravez = "s"
while otravez == "s":

    # Ejecutando Menú y camturando parametros

    l = menu()
    n = int(l[0])
    t = int(l[1])
    simul = l[2]

    # Registro de movimientos y aplicacion de Hanoi

    mov = []
    hanoi(n, "A", "C", "B")

    if simul == "s":
        # Creación de Discos y Postes
        A = []
        B = []
        C = []
        for i in range(1, 2 * n, 2):
            A.append('{:^20}'.format('*' * i))

        for _ in range(n):
            B.append('{:^20}'.format('|'))

        for _ in range(n):
            C.append('{:^20}'.format('|'))

        # Impresion de movimientos en consola

        cuenta = 0
        print('{:^20}'.format('A'), '{:^20}'.format('B'), '{:^20}'.format('C'))
        for x in range(n):
            print(A[x], B[x], C[x])
        print("Movimientos:", cuenta)
        for y in mov:
            mover_dic(y)
            time.sleep(t)
            print('{:-^80}'.format("-"))
            print("Moviendo disco", y[0], "de", y[1], "a", y[2])
            print('{:^20}'.format('A'), '{:^20}'.format('B'), '{:^20}'.format('C'))
            for x in range(n):
                print(A[x], B[x], C[x])
            cuenta = cuenta + 1
            print("Movimientos:", cuenta)

        g = False
        while not g:
            otravez = input("¿Volver al menú? s/n: ")
            if otravez == "s" or otravez == "n":
                g = True
            else:
                print("Ingrese \"s\" para sí o \"n\" para no")

    else:
        otravez = "n"

print('{:-^80}'.format("Programa Finalizado"))