# Universidad de San Carlos de Guatemala
# Escuela de Ciencias Físicas y Matemáticas
# Programación Matemática 1
# Luis José Velásquez Berdúo
# 20121338
# Problema codechef College Life 5
# contar la cantidad de veces que se cambia de canal

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    F = input().split()
    C = input().split()

    i = 0
    j = 0

    if int(F[0]) < int(C[0]):
        cambiar_canal = 0
        while i < N and j < M:
            if cambiar_canal % 2 == 0:
                if int(F[i]) < int(C[j]):
                    cambiar_canal += 1
                    i += 1
                else:
                    j +=1
            else:
                if int(C[j]) < int(F[i]):
                    cambiar_canal += 1
                    j += 1
                else:
                    i += 1
    if int(C[0]) < int(F[0]):
        cambiar_canal = 1
        while i < N and j < M:
            if cambiar_canal % 2 == 0:
                if int(F[i]) < int(C[j]):
                    cambiar_canal += 1
                    i += 1
                else:
                    j +=1
            else:
                if int(C[j]) < int(F[i]):
                    cambiar_canal += 1
                    j += 1
                else:
                    i += 1

    print(cambiar_canal)