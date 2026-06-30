# -*- coding: utf-8 -*-
from validador import validar_email, EmailInvalido

for c in ["ana@mail.com", "ana.mail.com"]:
    try:
        print("Válido:", validar_email(c))
    except EmailInvalido as e:
        print("Error:", e)
