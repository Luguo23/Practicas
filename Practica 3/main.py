#Universidad de San Carlos de Guatemala
#Escuela de Ciencia Físicas y Matemáticas
#Programación Matemática 1
#Luis José Velásquez Berdúo
#201213358

from ps4b import PlaintextMessage
from ps4b import CiphertextMessage
from ps4c import SubMessage
from ps4c import EncryptedSubMessage

def obtener_texto(nombre_archivo):
    print("Cargando archivo", nombre_archivo, " ...")
    texto = []
    with open(nombre_archivo, 'r') as file:
        for linea in file:
            texto.append(linea.strip("\n"))
    return texto

def encriptar_cesar(texto, k):
    cifrado = PlaintextMessage(texto, k)
    cifrado.get_shift()
    return cifrado.get_message_text_encrypted()

def desenciptar_cesar(texto):
    cifrado = CiphertextMessage(texto)
    return cifrado.decrypt_message()

def encriptar_sustitucion(texto, permutacion):
    cifrado = SubMessage(texto)
    dic_aux = cifrado.build_transpose_dict(permutacion)
    return cifrado.apply_transpose(dic_aux)

def desencriptar_sustitucion(texto):
    cifrado = EncryptedSubMessage(texto)
    return cifrado.decrypt_message()

otra_vez = "s"
while otra_vez == "s":
    print('{:-^80}'.format("Cifrado Cesar y Cifrado por Sustitución"))
    print("Elija una opción:\n 1 Encriptar con Cifrado Cesar\n 2 Encriptar con Cifrado por Sustitución\n 3 Desencriptar")
    op = input("Ingrese el número de opción >> ")
    if op == "1":
        print('{:-^80}'.format("Cifrado Cesar"))
        p = True
        while p:
            print(" 1 Escribir mensaje en consola\n 2 Cargar un archivo")
            opc = input("Ingrese el número de opción >> ")
            if opc == "1":
                p = False
                k = int(input("Ingrese un número entero para el cifrado: "))
                texto = input("Esciba el mensaje que desea codificar: ")
                print("Mensaje con Cifrado Cesar:")
                print(">>", encriptar_cesar(texto, k))
            elif opc == "2":
                p = False
                k = int(input("Ingrese un número entero para el cifrado: "))
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                texto = obtener_texto(nombre_archivo)
                print("Mensaje sin cifrar:")
                for linea in texto:
                    print(">>", linea)
                print("Mensaje con Cifrado Cesar: ")
                for linea in texto:
                    print(">>", encriptar_cesar(linea, k))
            else:
                print(opc, "No es opcion, vuelva a intentar")

    elif op == "2":
        print('{:-^80}'.format("Cifrado por Sustitución"))
        q = True
        while q:
            print(" 1 Escribir mensaje en consola\n 2 Cargar un archivo")
            ops = input("Ingrese el número de opción >> ")
            if ops == "1":
                q = False
                permutacion = input("Ingrese la secuencia de cinco vocales para sustituir \"aeiou\": ")
                texto = input("Escriba el mensaje que desea codificar: ")
                print("Mensaje con Cifrado por Sustitucion:")
                print(encriptar_sustitucion(texto, permutacion))
            elif ops == "2":
                q = False
                permutacion = input("Ingrese la secuencia de cinco vocales para sustituir \"aeiou\": ")
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                texto = obtener_texto(nombre_archivo)
                print("Mensaje sin cifrar:")
                for linea in texto:
                    print(">>", linea)
                print("Mensaje con Cifrado por Sustitucion:")
                for linea in texto:
                    print(">>", encriptar_sustitucion(linea, permutacion))
            else:
                print(ops, "No es opcion, vuelva a intentar")

    elif op == "3":
        print('{:-^80}'.format("Desencriptar"))
        r = True
        while r:
            print(" 1 Escribir mensaje en consola\n 2 Cargar un archivo")
            opd = input("Ingrese el número de opción >> ")
            if opd == "1":
                r = False
                texto = input("Igrese mensaje a decifrar: ")
                clave = desencriptar_sustitucion(texto)
                valor = True
                for x in clave.split():
                    if x in texto.split():
                        valor = False
                if valor:
                    print("El mensaje estaba cifrado con Cifrado por Sustitución")
                    print(">>", clave)
                else:
                    print("El mensaje estaba cifrado con Cifrado Cesar")
                    print(">>", desenciptar_cesar(texto)[1])

            elif opd == "2":
                r = False
                nombre_archivo = input("Ingrese el nombre del archivo: ")
                texto = obtener_texto(nombre_archivo)
                clave = desencriptar_sustitucion(texto[0])
                valor = True
                for x in clave.split():
                    if x in texto[0].split():
                        valor = False
                if valor:
                    print("El mensaje estaba cifrado con Cifrado por Sustitución")
                    for linea in texto:
                        print(">>", desencriptar_sustitucion(linea))
                else:
                    print("El mensaje estaba cifrado con Cifrado Cesar")
                    for linea in texto:
                        print(">>", desenciptar_cesar(linea)[1])
            else:
                print(opd, "No es una opcion")
    else:
        print(op, "No es una opcion")
    otra_vez = input("¿Desea volver al menú principal? s/n : ")
    if otra_vez != "s":
        print('{:-^80}'.format("Fin del programa"))