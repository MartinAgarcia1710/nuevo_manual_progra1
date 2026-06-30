# -*- coding: utf-8 -*-
def manejar(operacion):
    """Ejecuta una operación (función) y devuelve un mensaje según el error."""
    try:
        return operacion()
    except ZeroDivisionError:
        return "Error: división por cero"
    except ValueError:
        return "Error: valor inválido"
    except IndexError:
        return "Error: índice fuera de rango"
    except Exception as e:
        return f"Error inesperado: {e}"
