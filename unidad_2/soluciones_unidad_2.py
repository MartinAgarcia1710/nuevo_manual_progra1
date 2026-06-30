# -*- coding: utf-8 -*-
"""
Soluciones - Unidad 2: Estructuras condicionales
Programación 1 - UTN - Autor: Martín Alejandro García
"""


def ejercicio_1():
    """Par o impar."""
    n = int(input("Número entero: "))
    if n % 2 == 0:
        print("Es par")
    else:
        print("Es impar")


def ejercicio_2():
    """Mayor o menor de edad."""
    edad = int(input("Edad: "))
    if edad >= 18:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")


def ejercicio_3():
    """Mayor de tres números."""
    a = float(input("a: ")); b = float(input("b: ")); c = float(input("c: "))
    if a >= b and a >= c:
        print(f"El mayor es {a}")
    elif b >= c:
        print(f"El mayor es {b}")
    else:
        print(f"El mayor es {c}")


def ejercicio_4():
    """Signo del número."""
    n = float(input("Número: "))
    if n > 0:
        print("Positivo")
    elif n < 0:
        print("Negativo")
    else:
        print("Cero")


def ejercicio_5():
    """Año bisiesto."""
    anio = int(input("Año: "))
    if anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0):
        print("Es bisiesto")
    else:
        print("No es bisiesto")


def ejercicio_6():
    """Categoría por IMC."""
    imc = float(input("IMC: "))
    if imc < 18.5:
        print("Bajo peso")
    elif imc < 25:
        print("Normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")


def ejercicio_7():
    """Descuento según el monto de la compra."""
    total = float(input("Total de la compra: $"))
    if total > 10000:
        descuento = 0.15
    elif total > 5000:
        descuento = 0.10
    else:
        descuento = 0.0
    final = total * (1 - descuento)
    print(f"Descuento: {int(descuento * 100)}% - Total: ${final:.2f}")


def ejercicio_8():
    """Aprobado o desaprobado."""
    nota = float(input("Nota (0-10): "))
    if nota >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


def ejercicio_9():
    """Vocal o consonante."""
    letra = input("Una letra: ").lower()
    if letra in "aeiou":
        print("Es vocal")
    else:
        print("Es consonante")


def ejercicio_10():
    """Calculadora con match-case."""
    a = float(input("a: ")); b = float(input("b: "))
    op = input("Operación (+, -, *, /): ")
    match op:
        case "+":
            print(a + b)
        case "-":
            print(a - b)
        case "*":
            print(a * b)
        case "/":
            print(a / b if b != 0 else "No se puede dividir por cero")
        case _:
            print("Operación inválida")


def ejercicio_11():
    """Mayor y menor de tres números."""
    a = float(input("a: ")); b = float(input("b: ")); c = float(input("c: "))
    mayor = max(a, b, c)
    menor = min(a, b, c)
    print(f"Mayor: {mayor} - Menor: {menor}")


def ejercicio_12():
    """Número dentro del rango 1 a 100."""
    n = int(input("Número: "))
    if 1 <= n <= 100:
        print("Está dentro del rango")
    else:
        print("Está fuera del rango")


def ejercicio_13():
    """Triángulo válido."""
    a = float(input("Lado a: ")); b = float(input("Lado b: ")); c = float(input("Lado c: "))
    if a < b + c and b < a + c and c < a + b:
        print("Pueden formar un triángulo")
    else:
        print("No pueden formar un triángulo")


def ejercicio_14():
    """Día de la semana con match-case."""
    n = int(input("Número del día (1-7): "))
    match n:
        case 1: print("Lunes")
        case 2: print("Martes")
        case 3: print("Miércoles")
        case 4: print("Jueves")
        case 5: print("Viernes")
        case 6: print("Sábado")
        case 7: print("Domingo")
        case _: print("Número fuera de rango")


def ejercicio_15():
    """Login simple con usuario y contraseña fijos."""
    USUARIO = "admin"
    CLAVE = "1234"
    u = input("Usuario: ")
    c = input("Contraseña: ")
    if u == USUARIO and c == CLAVE:
        print("Acceso correcto")
    else:
        print("Acceso denegado")


def ejercicio_16():
    """Tarifa de estacionamiento."""
    horas = int(input("Cantidad de horas: "))
    if horas <= 0:
        print("Cantidad inválida")
    else:
        total = 500 + (horas - 1) * 300
        print(f"Total a pagar: ${total}")


def ejercicio_17():
    """Acción según el color del semáforo."""
    color = input("Color (rojo/amarillo/verde): ").lower()
    if color == "rojo":
        print("Frenar")
    elif color == "amarillo":
        print("Precaución")
    elif color == "verde":
        print("Avanzar")
    else:
        print("Color inválido")


def ejercicio_18():
    """¿El primero es múltiplo del segundo?"""
    a = int(input("Primer número: ")); b = int(input("Segundo número: "))
    if b != 0 and a % b == 0:
        print(f"{a} es múltiplo de {b}")
    else:
        print(f"{a} no es múltiplo de {b}")


def ejercicio_19():
    """Comparar dos números."""
    a = float(input("a: ")); b = float(input("b: "))
    if a == b:
        print("Son iguales")
    elif a > b:
        print(f"{a} es mayor")
    else:
        print(f"{b} es mayor")


def ejercicio_20():
    """Clasificar un carácter."""
    c = input("Un carácter: ")
    if c.isdigit():
        print("Es un dígito")
    elif c.isalpha():
        print("Es una letra")
    else:
        print("Es un símbolo")


if __name__ == "__main__":
    pass
