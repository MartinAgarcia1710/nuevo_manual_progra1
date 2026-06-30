# Soluciones — Unidad 4: Trabajo colaborativo (Git)

Estos ejercicios se resuelven con **comandos de Git** en la terminal, no con Python.
A continuación, los comandos y explicaciones de referencia para cada uno.

---

## Ejercicio 1 — Crear un repositorio
```bash
mkdir mi_proyecto
cd mi_proyecto
git init
git status
```

## Ejercicio 2 — Primer commit
```bash
echo 'print("Hola")' > programa.py
git add programa.py
git commit -m "Agrega el programa inicial"
```

## Ejercicio 3 — Configurar identidad
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@correo.com"
```

## Ejercicio 4 — Archivo .gitignore
```
# .gitignore
venv/
__pycache__/
*.log
```

## Ejercicio 5 — Historial de cambios
```bash
git add archivo.py && git commit -m "Cambio 1"
git add archivo.py && git commit -m "Cambio 2"
git add archivo.py && git commit -m "Cambio 3"
git log --oneline
```

## Ejercicio 6 — Deshacer cambios
```bash
git restore archivo.py     # descarta cambios no confirmados
# (alternativa antigua): git checkout -- archivo.py
```

## Ejercicio 7 — Clonar un repositorio
```bash
git clone https://github.com/usuario/proyecto.git
cd proyecto
```

## Ejercicio 8 — Conectar con remoto
```bash
git remote add origin https://github.com/usuario/proyecto.git
git branch -M main
git push -u origin main
```

## Ejercicio 9 — Crear una rama
```bash
git branch nueva-funcion
git checkout nueva-funcion     # o: git switch nueva-funcion
git add . && git commit -m "Trabajo en la nueva función"
```

## Ejercicio 10 — Fusionar ramas
```bash
git checkout main
git merge nueva-funcion
```

## Ejercicio 11 — Ver diferencias
```bash
git diff       # muestra, línea por línea, lo que cambió respecto del último commit
```

## Ejercicio 12 — Flujo completo
```bash
# 1. Editar archivos en el editor
git status                 # ver qué cambió
git add .                  # preparar los cambios
git commit -m "Descripción clara del cambio"
git push                   # subir al remoto
```

## Ejercicio 13 — Mensajes de commit (ejemplos)
- `git commit -m "Corrige el cálculo del promedio"`
- `git commit -m "Agrega validación de edad en el formulario"`
- `git commit -m "Elimina código duplicado en utilidades"`
- `git commit -m "Actualiza el README con instrucciones de uso"`
- `git commit -m "Agrega manejo de errores al leer archivos"`

## Ejercicio 14 — Recuperar una versión
```bash
git log --oneline          # obtener el identificador del commit
git show a1b2c3d           # ver ese commit en detalle
git checkout a1b2c3d -- archivo.py   # recuperar una versión anterior de un archivo
```

## Ejercicio 15 — Trabajo en equipo
```bash
git pull                   # traer e integrar los cambios del remoto antes de empezar
```

## Ejercicio 16 — Resolver un conflicto
Un **conflicto de fusión** ocurre cuando dos personas modificaron las mismas líneas.
Git marca la zona en disputa así:
```
<<<<<<< HEAD
mi versión
=======
versión del otro
>>>>>>> rama
```
Se resuelve editando el archivo para dejar la versión correcta, borrando las marcas, y luego:
```bash
git add archivo.py
git commit
```

## Ejercicio 17 — README del proyecto
```bash
echo "# Mi Proyecto" > README.md
git add README.md
git commit -m "Agrega README del proyecto"
```

## Ejercicio 18 — Estado del repositorio
`git status` muestra: la rama actual, los archivos modificados sin preparar,
los archivos preparados para el próximo commit y los archivos sin seguimiento.
Conviene usarlo antes de cada `add` y `commit` para saber exactamente qué se va a guardar.

## Ejercicio 19 — Etiquetas de versión
```bash
git tag v1.0
git push origin v1.0
```
Una etiqueta (tag) marca un punto importante de la historia, como una versión publicada.

## Ejercicio 20 — Buenas prácticas (cinco)
1. Hacer commits pequeños y frecuentes, con un cambio lógico cada uno.
2. Escribir mensajes de commit claros y en presente.
3. Hacer `git pull` antes de empezar a trabajar para evitar conflictos.
4. Usar ramas para nuevas funcionalidades y no trabajar directo sobre `main`.
5. Mantener un `.gitignore` para no subir archivos innecesarios o sensibles.
