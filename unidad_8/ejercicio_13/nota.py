# -*- coding: utf-8 -*-
class NotaInvalida(Exception):
    pass

def validar_nota(nota):
    if nota < 0 or nota > 10:
        raise NotaInvalida("La nota debe estar entre 0 y 10")
    return nota
