# -*- coding: utf-8 -*-
"""
Soluciones - Unidad 1: Estructuras secuenciales
Programación 1 - UTN - Autor: Martín Alejandro García

Cada ejercicio está resuelto en una función. Para probar uno, llamalo al final
del archivo, por ejemplo: ejercicio_2()
"""


def ejercicio_1():
    """Hola con nombre."""
    nombre = input("¿Cómo te llamás? ")
    print(f"¡Hola, {nombre}! Bienvenido/a a Programación 1.")


def ejercicio_2():
    """Suma, resta, multiplicación y división de dos números."""
    a = int(input("Primer número: "))
    b = int(input("Segundo número: "))
    print(f"Suma: {a + b}")
    print(f"Resta: {a - b}")
    print(f"Multiplicación: {a * b}")
    print(f"División: {a / b}")


def ejercicio_3():
    """Área y perímetro de un rectángulo."""
    base = float(input("Base (cm): "))
    altura = float(input("Altura (cm): "))
    print(f"Área: {base * altura} cm²")
    print(f"Perímetro: {2 * (base + altura)} cm")


def ejercicio_4():
    """Convertir grados Celsius a Fahrenheit."""
    celsius = float(input("Temperatura en °C: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"{celsius} °C equivalen a {fahrenheit} °F")


def ejercicio_5():
    """Precio final con 21% de IVA."""
    precio = float(input("Precio sin IVA: $"))
    final = precio * 1.21
    print(f"Precio final con IVA: ${final:.2f}")


def ejercicio_6():
    """Promedio de tres notas con dos decimales."""
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    n3 = float(input("Nota 3: "))
    promedio = (n1 + n2 + n3) / 3
    print(f"Promedio: {promedio:.2f}")


def ejercicio_7():
    """Convertir una cantidad de segundos a horas, minutos y segundos."""
    total = int(input("Cantidad de segundos: "))
    horas = total // 3600
    minutos = (total % 3600) // 60
    segundos = total % 60
    print(f"{horas} h, {minutos} min, {segundos} s")


def ejercicio_8():
    """Intercambiar el contenido de dos variables."""
    a = input("Valor A: ")
    b = input("Valor B: ")
    print(f"Antes -> A: {a}, B: {b}")
    a, b = b, a
    print(f"Después -> A: {a}, B: {b}")


def ejercicio_9():
    """Edad aproximada en días."""
    anios = int(input("Edad en años: "))
    print(f"Viviste aproximadamente {anios * 365} días.")


def ejercicio_10():
    """Perímetro y área de un círculo."""
    PI = 3.14159
    radio = float(input("Radio: "))
    print(f"Perímetro: {2 * PI * radio:.2f}")
    print(f"Área: {PI * radio ** 2:.2f}")


def ejercicio_11():
    """Mostrar una palabra en mayúsculas, minúsculas y capitalizada."""
    palabra = input("Escribí una palabra: ")
    print("Mayúsculas:", palabra.upper())
    print("Minúsculas:", palabra.lower())
    print("Capitalizada:", palabra.capitalize())


def ejercicio_12():
    """Cantidad de caracteres de una frase."""
    frase = input("Escribí una frase: ")
    print(f"La frase tiene {len(frase)} caracteres.")


def ejercicio_13():
    """Convertir dólares a pesos según la cotización."""
    dolares = float(input("Monto en dólares: "))
    cotizacion = float(input("Cotización del dólar: "))
    print(f"Equivalen a ${dolares * cotizacion:.2f}")


def ejercicio_14():
    """Descomponer un importe en billetes de 1000, 100 y monedas de 1."""
    importe = int(input("Importe entero: "))
    billetes_1000 = importe // 1000
    resto = importe % 1000
    billetes_100 = resto // 100
    monedas = resto % 100
    print(f"Billetes de 1000: {billetes_1000}")
    print(f"Billetes de 100: {billetes_100}")
    print(f"Monedas de 1: {monedas}")


def ejercicio_15():
    """Promedio de dos enteros con un decimal."""
    a = int(input("Primer entero: "))
    b = int(input("Segundo entero: "))
    print(f"Promedio: {(a + b) / 2:.1f}")


def ejercicio_16():
    """Saludo formal con apellido y nombre."""
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    print(f"Estimado/a, {apellido} {nombre}.")


def ejercicio_17():
    """Calcular propina del 10% y el total."""
    total = float(input("Total de la cuenta: $"))
    propina = total * 0.10
    print(f"Propina (10%): ${propina:.2f}")
    print(f"Total a pagar: ${total + propina:.2f}")


def ejercicio_18():
    """Distancia recorrida a partir de velocidad y tiempo."""
    velocidad = float(input("Velocidad (km/h): "))
    tiempo = float(input("Tiempo (h): "))
    print(f"Distancia recorrida: {velocidad * tiempo} km")


def ejercicio_19():
    """Índice de masa corporal."""
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    imc = peso / altura ** 2
    print(f"Tu IMC es {imc:.2f}")


def ejercicio_20():
    """Ticket de compra con subtotal."""
    producto = input("Producto: ")
    precio = float(input("Precio unitario: $"))
    cantidad = int(input("Cantidad: "))
    print("----- TICKET -----")
    print(f"{producto} x {cantidad}")
    print(f"Subtotal: ${precio * cantidad:.2f}")


if __name__ == "__main__":
    # Descomentá el ejercicio que quieras probar:
    # ejercicio_1()
    pass
