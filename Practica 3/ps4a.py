# Problem Set 4A
# Name: Luis José Velásquez Berdúo
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    if len(sequence) <= 1:
        return [sequence]
    else:
        permutaciones = []
        for i in range(len(sequence)):
            letra = sequence[i]
            resto = sequence[0: i] + sequence[i + 1:]
            per = get_permutations(resto)
            for j in per:
                if letra + j not in permutaciones:
                    permutaciones.append(letra + j)
        return permutaciones


#Ejemplos


if __name__ == '__main__':
    print(get_permutations("casa"))

    print(get_permutations("cat"))

    print(get_permutations("bat"))
