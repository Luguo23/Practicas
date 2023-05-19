# Universidad de San Carlos de Guatemala
# Escuela de Ciencias Físicas y Matemáticas
# Programación Matemática 1
# Luis José Velásquez Berdúo
# 20121338

# Si P es el perimetro de un tringulo rectangulo con lados enteros {a,b,c}
# hay exactamento tres soluciones para P = 120 {20,48,52}, {24,45,51}, {30,40,50}
# ¿para que valor de p <= 1000, el numero de soluciones es maximo?

valor_p = 0
nsoluciones = 0

# Solución: Notar que si los lados del triangulo rectangulo son enteros entonces forzosamente a,b,c tienen que ser
# distintos entre si y de la misma manera c > a y c > b.
# Tambien los lados del triangulo pueden ser representados como a = qP , b = rP y c = sP donde q + r + s = 1
# y deben cumplir con c^2 = a^2 + b^2, teniendo esto encuenta podemos hacer.

for p in range(1,1000):
    cuenta_solucion = 0

    if p%3 == 0:

        # Elegimos arbitrariamente el lado "a" como el más pequeño, entonces la cota superior de "a" es P/3

        for a in range(1, p//3):

            # Como "a" es el lado más pequeño y c > b, entonces b es esta acotado por el valor de c
            # la cota inferior de "c" es P/3, por lo que la cota de "b" en funcion de "a" es b = (2/3)*P - a

            for b in range(a, 2*(p//3) - a):

                # Calculamos el valor de c y comprobamos la condicion de triangulo rectangulo

                c = p - a - b
                if c**2 == a**2 + b**2:
                    cuenta_solucion += 1
        if nsoluciones < cuenta_solucion:
            nsoluciones = cuenta_solucion
            valor_p = p

print(nsoluciones, valor_p)

