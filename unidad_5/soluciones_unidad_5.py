# -*- coding: utf-8 -*-
"""
Soluciones - Unidad 5: Listas
Programación 1 - UTN - Autor: Martín Alejandro García
"""


def ejercicio_1():
    """Cargar 5 números en una lista y mostrarla."""
    numeros = []
    for i in range(5):
        numeros.append(int(input(f"Número {i + 1}: ")))
    print("Lista:", numeros)


def ejercicio_2():
    """Suma de los elementos de una lista."""
    numeros = [10, 25, 3, 47, 8]
    total = 0
    for n in numeros:
        total += n
    print("Suma:", total)


def ejercicio_3():
    """Promedio de una lista de notas."""
    notas = [7, 9, 4, 8, 10]
    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")


def ejercicio_4():
    """Máximo y mínimo sin usar max() ni min()."""
    numeros = [12, 5, 47, 8, 33]
    mayor = menor = numeros[0]
    for n in numeros:
        if n > mayor:
            mayor = n
        if n < menor:
            menor = n
    print(f"Mayor: {mayor} - Menor: {menor}")


def ejercicio_5():
    """Mostrar una lista en orden inverso."""
    numeros = [1, 2, 3, 4, 5]
    for i in range(len(numeros) - 1, -1, -1):
        print(numeros[i], end=" ")
    print()


def ejercicio_6():
    """Buscar un valor e indicar su posición."""
    numeros = [10, 20, 30, 40, 50]
    valor = int(input("Valor a buscar: "))
    if valor in numeros:
        print(f"Está en la posición {numeros.index(valor)}")
    else:
        print("No está en la lista")


def ejercicio_7():
    """Contar apariciones de un valor."""
    numeros = [1, 2, 2, 3, 2, 4, 2]
    valor = 2
    print(f"El {valor} aparece {numeros.count(valor)} veces")


def ejercicio_8():
    """Separar pares e impares en dos listas."""
    numeros = [4, 7, 10, 13, 2, 9]
    pares = []
    impares = []
    for n in numeros:
        if n % 2 == 0:
            pares.append(n)
        else:
            impares.append(n)
    print("Pares:", pares)
    print("Impares:", impares)


def ejercicio_9():
    """Eliminar duplicados de una lista."""
    numeros = [1, 2, 2, 3, 3, 3, 4]
    sin_repetidos = []
    for n in numeros:
        if n not in sin_repetidos:
            sin_repetidos.append(n)
    print("Sin duplicados:", sin_repetidos)


def ejercicio_10():
    """Ordenar una lista de menor a mayor."""
    numeros = [50, 12, 7, 33, 8, 21]
    numeros.sort()
    print("Ordenada:", numeros)


def ejercicio_11():
    """Sumar dos listas elemento a elemento."""
    a = [1, 2, 3, 4]
    b = [10, 20, 30, 40]
    suma = []
    for i in range(len(a)):
        suma.append(a[i] + b[i])
    print("Suma elemento a elemento:", suma)


def ejercicio_12():
    """Lista con los cuadrados del 1 al 10."""
    cuadrados = []
    for i in range(1, 11):
        cuadrados.append(i ** 2)
    print(cuadrados)


def ejercicio_13():
    """Cantidad de elementos que superan un umbral."""
    numeros = [3, 8, 15, 22, 5, 19]
    umbral = 10
    cantidad = 0
    for n in numeros:
        if n > umbral:
            cantidad += 1
    print(f"{cantidad} elementos superan {umbral}")


def ejercicio_14():
    """Concatenar nombres separados por comas."""
    nombres = ["Ana", "Bruno", "Carla", "Diego"]
    print(", ".join(nombres))


def ejercicio_15():
    """Rotar una lista: el primero pasa al final."""
    numeros = [1, 2, 3, 4, 5]
    primero = numeros.pop(0)
    numeros.append(primero)
    print("Rotada:", numeros)


def ejercicio_16():
    """Segundo elemento más grande."""
    numeros = [12, 45, 7, 45, 33, 9]
    unicos = sorted(set(numeros))
    if len(unicos) >= 2:
        print("Segundo más grande:", unicos[-2])
    else:
        print("No hay segundo valor distinto")


def ejercicio_17():
    """Promedio descartando el valor más bajo."""
    numeros = [8, 4, 10, 6, 9]
    sin_menor = numeros.copy()
    sin_menor.remove(min(sin_menor))
    print(f"Promedio sin el menor: {sum(sin_menor) / len(sin_menor):.2f}")


def ejercicio_18():
    """Crear y mostrar una matriz 3x3."""
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for fila in matriz:
        for valor in fila:
            print(valor, end=" ")
        print()


def ejercicio_19():
    """Suma de la diagonal principal de una matriz 3x3."""
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    suma = 0
    for i in range(3):
        suma += matriz[i][i]
    print("Suma de la diagonal:", suma)


def ejercicio_20():
    """Invertir una lista usando slicing."""
    numeros = [1, 2, 3, 4, 5]
    print("Invertida:", numeros[::-1])


if __name__ == "__main__":
    # Ejercicios sin input que se pueden correr directo:
    for f in [ejercicio_2, ejercicio_3, ejercicio_4, ejercicio_5, ejercicio_7,
              ejercicio_8, ejercicio_9, ejercicio_10, ejercicio_11, ejercicio_12,
              ejercicio_13, ejercicio_14, ejercicio_15, ejercicio_16, ejercicio_17,
              ejercicio_18, ejercicio_19, ejercicio_20]:
        print(f"\n--- {f.__name__} ---")
        f()
