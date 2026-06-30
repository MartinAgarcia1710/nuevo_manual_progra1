# Soluciones — Unidad 0: Introducción y primeros pasos

Estos ejercicios no se resuelven con código Python, sino expresando algoritmos en
**lenguaje coloquial** o **pseudocódigo**. A continuación, una solución de referencia
para cada uno. Recordá que puede haber varias formas válidas de escribir un algoritmo.

---

## Ejercicio 1 — Preparar un mate
1. Llenar la pava con agua.
2. Poner la pava a calentar.
3. Mientras el agua no esté caliente (sin llegar a hervir), esperar.
4. Colocar la yerba en el mate hasta unos tres cuartos de su capacidad.
5. Tapar el mate con la mano, darlo vuelta y agitarlo suavemente.
6. Volver el mate a su posición e inclinar la yerba hacia un costado.
7. Colocar la bombilla del lado con menos yerba.
8. Verter un poco de agua tibia para humedecer la yerba y esperar unos segundos.
9. Verter el agua caliente.
10. Entregar el mate a la persona.

## Ejercicio 2 — Lavarse los dientes
1. Tomar el cepillo de dientes.
2. Abrir la canilla y mojar el cepillo.
3. Abrir la pasta dental.
4. Colocar una porción de pasta sobre el cepillo.
5. Cerrar la pasta.
6. Cepillar los dientes superiores con movimientos suaves durante dos minutos.
7. Cepillar los dientes inferiores.
8. Cepillar la lengua.
9. Enjuagarse la boca con agua.
10. Enjuagar el cepillo y guardarlo.
11. Cerrar la canilla.

## Ejercicio 3 — Cruzar la calle
1. Acercarse al borde de la vereda.
2. Observar el semáforo peatonal.
3. SI el semáforo está en rojo:
   - Esperar.
   - Volver al paso 2.
4. SI el semáforo está en verde:
   - Mirar a ambos lados para confirmar que no vienen vehículos.
   - Cruzar caminando por la senda peatonal.
5. Llegar a la vereda de enfrente.

## Ejercicio 4 — Hacer un café instantáneo
1. Calentar agua hasta que esté bien caliente.
2. Colocar una taza sobre la mesada.
3. Agregar una cucharada de café instantáneo en la taza.
4. Agregar azúcar a gusto (opcional).
5. Verter el agua caliente en la taza.
6. Revolver con una cuchara hasta disolver.
7. Servir.

## Ejercicio 5 — Cajero automático (pseudocódigo)
```
INICIO
    Insertar la tarjeta
    LEER pin
    SI pin es incorrecto ENTONCES
        MOSTRAR "PIN incorrecto"
        TERMINAR
    FIN SI
    LEER monto a extraer
    SI monto <= saldo ENTONCES
        Entregar el dinero
        saldo = saldo - monto
        MOSTRAR "Operación exitosa"
    SINO
        MOSTRAR "Saldo insuficiente"
    FIN SI
    Devolver la tarjeta
FIN
```

## Ejercicio 6 — Mayor de dos números (pseudocódigo)
```
INICIO
    LEER a, b
    SI a > b ENTONCES
        MOSTRAR a, "es el mayor"
    SINO SI b > a ENTONCES
        MOSTRAR b, "es el mayor"
    SINO
        MOSTRAR "Son iguales"
    FIN SI
FIN
```

## Ejercicio 7 — Promedio de tres notas (pseudocódigo)
```
INICIO
    LEER nota1, nota2, nota3
    promedio = (nota1 + nota2 + nota3) / 3
    MOSTRAR "El promedio es:", promedio
FIN
```

## Ejercicio 8 — Encender la computadora
1. Presionar el botón de encendido.
2. Esperar a que el sistema operativo cargue.
3. SI pide usuario y contraseña: ingresarlos.
4. Esperar a que aparezca el escritorio.
5. Buscar el ícono del programa deseado.
6. Hacer doble clic sobre el ícono.
7. Esperar a que el programa abra.

## Ejercicio 9 — Preparar fideos
1. Llenar una olla con agua.
2. Poner la olla al fuego.
3. Esperar a que el agua hierva.
4. Agregar sal.
5. Agregar los fideos.
6. Mientras no pase el tiempo indicado en el paquete, revolver de vez en cuando.
7. Apagar el fuego.
8. Colar los fideos.
9. Servir.

## Ejercicio 10 — Enviar un mensaje
1. Desbloquear el celular.
2. Abrir la aplicación de mensajes.
3. Buscar el contacto deseado.
4. Tocar el contacto para abrir la conversación.
5. Escribir el mensaje.
6. Presionar el botón de enviar.
7. Verificar que el mensaje se haya enviado.

## Ejercicio 11 — Pagar en efectivo en un kiosco
1. Elegir el producto.
2. Preguntar el precio.
3. Buscar el dinero en la billetera.
4. SI el dinero alcanza:
   - Entregar el dinero al vendedor.
   - SI se pagó de más: recibir el vuelto.
   - Retirar el producto.
5. SINO:
   - Devolver el producto o elegir uno más barato.

## Ejercicio 12 — Número par o impar (coloquial)
Para decidir si un número es par: lo divido por 2 y miro el resto.
Si el resto de dividirlo por 2 es 0, el número es **par**.
Si el resto es 1, el número es **impar**.

## Ejercicio 13 — Armar una mochila para clases
1. Tomar la mochila vacía.
2. Para cada elemento de la lista (cuadernos, lápices, libros, cargador, botella):
   - Verificar si está.
   - SI está: guardarlo en la mochila.
   - SI no está: buscarlo y luego guardarlo.
3. Cerrar la mochila.

## Ejercicio 14 — Cambiar una lámpara
1. Apagar la luz desde la llave.
2. Cortar la electricidad de ese ambiente (precaución).
3. Esperar a que la lámpara quemada se enfríe.
4. Tomar una escalera si es necesario.
5. Desenroscar (o quitar) la lámpara quemada.
6. Colocar la lámpara nueva.
7. Restablecer la electricidad.
8. Encender la luz para verificar que funcione.

## Ejercicio 15 — El más alto de la fila (pseudocódigo)
```
INICIO
    mas_alto = primera persona de la fila
    PARA cada persona siguiente en la fila:
        SI persona es más alta que mas_alto ENTONCES
            mas_alto = persona
        FIN SI
    FIN PARA
    MOSTRAR mas_alto
FIN
```

## Ejercicio 16 — Receta de tostadas
1. Tomar dos rebanadas de pan.
2. Encender la tostadora.
3. Colocar las rebanadas en la tostadora.
4. Esperar a que estén doradas.
5. Retirar las tostadas.
6. Untar manteca sobre cada tostada.
7. Servir en un plato.

## Ejercicio 17 — Suma de los primeros N números (pseudocódigo)
```
INICIO
    LEER N
    suma = 0
    PARA i DESDE 1 HASTA N:
        suma = suma + i
    FIN PARA
    MOSTRAR suma
FIN
```

## Ejercicio 18 — Ordenar tres objetos por tamaño (coloquial)
1. Comparar la caja A con la B; quedarse con la más chica a la izquierda.
2. Comparar la caja del medio con la C; si C es más chica, intercambiarlas.
3. Volver a comparar las dos primeras por si cambió el orden.
4. Las tres cajas quedan ordenadas de menor a mayor.

## Ejercicio 19 — Llenar un vaso con agua (pseudocódigo)
```
INICIO
    Tomar un vaso
    SI la jarra está vacía ENTONCES
        MOSTRAR "No hay agua"
    SINO
        Inclinar la jarra sobre el vaso
        Verter hasta que el vaso esté lleno
        Enderezar la jarra
    FIN SI
FIN
```

## Ejercicio 20 — Decisión de llevar paraguas (pseudocódigo)
```
INICIO
    Observar el cielo
    SI está lloviendo ENTONCES
        Llevar paraguas
    SINO SI está nublado ENTONCES
        Llevar abrigo por las dudas
    SINO
        No llevar nada
    FIN SI
FIN
```
