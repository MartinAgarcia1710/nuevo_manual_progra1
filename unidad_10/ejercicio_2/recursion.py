# -*- coding: utf-8 -*-
def cuenta_regresiva(n):
    """Muestra una cuenta regresiva de n a 0."""
    if n < 0:
        return
    print(n)
    cuenta_regresiva(n - 1)
