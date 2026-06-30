# -*- coding: utf-8 -*-
from agenda import datos_contacto

agenda = {
    "Ana": {"tel": "111", "correo": "ana@mail.com"},
    "Leo": {"tel": "222", "correo": "leo@mail.com"},
}
print(datos_contacto(agenda, "Ana"))
