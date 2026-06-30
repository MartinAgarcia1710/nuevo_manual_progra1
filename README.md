# Soluciones — Manual de Prácticas · Programación 1 (UTN)

Autor: Martín Alejandro García

Este directorio contiene las soluciones de los **230 ejercicios** del Manual de Prácticas:
220 ejercicios (20 por unidad, de la 0 a la 10) y 10 prácticas integradoras.

## Organización

- **Unidades 0 a 5** → un único archivo por unidad con todos los ejercicios resueltos:
  - `unidad_0/soluciones_unidad_0.md` (algoritmos en pseudocódigo / lenguaje coloquial)
  - `unidad_1/soluciones_unidad_1.py` … `unidad_3/soluciones_unidad_3.py`
  - `unidad_4/soluciones_unidad_4.md` (comandos de Git)
  - `unidad_5/soluciones_unidad_5.py`

  En los archivos `.py`, cada ejercicio está resuelto en una función `ejercicio_N()`.
  Para probar uno, llamalo al final del archivo (por ejemplo, `ejercicio_3()`).

- **Unidades 6 a 10** → una carpeta por ejercicio, con un módulo y un `main.py`,
  para practicar el uso de módulos y paquetes. Por ejemplo:
  ```
  unidad_6/ejercicio_3/geometria.py
  unidad_6/ejercicio_3/main.py
  ```
  Para ejecutar: entrar a la carpeta del ejercicio y correr `python main.py`.

- **Integradoras** → una carpeta por proyecto, con sus módulos y un `main.py` que
  ejecuta una demostración:
  ```
  integradoras/integradora_1/gestion.py
  integradoras/integradora_1/main.py
  ```

## Nota sobre las soluciones

En las unidades 6 a 10 y en las integradoras, la lógica se escribió en funciones
"puras" (sin `input()`) dentro de los módulos, y cada `main.py` la demuestra con
datos de ejemplo. Esto permite ejecutar y verificar cada solución directamente.
La versión interactiva (con `input()` y menús) se construye llamando a esas mismas
funciones, como se indica en los enunciados.

Todas las soluciones de las unidades 6 a 10 y las integradoras fueron ejecutadas y
verificadas: corren sin errores.
