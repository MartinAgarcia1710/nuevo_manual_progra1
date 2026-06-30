# -*- coding: utf-8 -*-
class EmailInvalido(Exception):
    pass

def validar_email(correo):
    if "@" not in correo:
        raise EmailInvalido("Falta el símbolo @")
    return correo
