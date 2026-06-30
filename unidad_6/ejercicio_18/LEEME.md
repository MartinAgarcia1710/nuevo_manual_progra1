# Ejercicio 18 — Crear y usar un entorno virtual

```bash
# 1. Crear el entorno virtual
python -m venv venv

# 2. Activarlo
#    Windows:
venv\Scripts\activate
#    Linux / macOS:
source venv/bin/activate

# 3. Instalar una librería de terceros
pip install requests

# 4. Ver lo instalado y guardar las dependencias
pip list
pip freeze > requirements.txt

# 5. Desactivar el entorno
deactivate
```

Recordá agregar `venv/` al archivo `.gitignore` para no subirlo al repositorio.
