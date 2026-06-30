# -*- coding: utf-8 -*-
from log import registrar

registrar("registro.txt", "El programa se ejecutó")
registrar("registro.txt", "El programa se ejecutó otra vez")
print(open("registro.txt", encoding="utf-8").read())
