# -*- coding: utf-8 -*-
from seguridad import valida_password

for clave in ["abc", "abcdefgh", "abcd1234"]:
    print(f"{clave!r} -> válida: {valida_password(clave)}")
