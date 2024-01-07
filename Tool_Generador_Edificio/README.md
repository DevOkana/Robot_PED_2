
---

# Generador de Edificios y Exportador a Archivos de Texto

Este programa en Python consta de tres clases: `Edificio`, `Exportar`, y `GeneratorArchivo`, diseñadas para generar edificios aleatorios y exportar la información a archivos de texto.

## Clases

### 1. Edificio

La clase `Edificio` representa un edificio con pasillos, tornillos y espacios reducidos. Algunas características clave:

- Matriz que representa el edificio.
- Generación aleatoria de filas y columnas.
- Colocación aleatoria de un tornillo en el edificio.
- Exportación de la información del edificio.

### 2. Exportar

La clase `Exportar` maneja la exportación de la información del edificio a archivos de texto. Características notables:

- Contador compartido para nombrar los archivos de manera única.
- Verificación de existencia del archivo antes de la exportación.
- Creación de una carpeta para almacenar los archivos de entrada.
- Escritura de datos del edificio en archivos de texto.

### 3. GeneratorArchivo

La clase `GeneratorArchivo` se utiliza para generar múltiples archivos de edificios. Características destacadas:

- Inicialización con la cantidad deseada de archivos a generar.
- Uso de la clase `Exportar` para generar y exportar edificios en archivos de texto.

## Uso

1. Ejecuta el script para generar archivos de edificios.
2. Los archivos se almacenarán en la carpeta "entrada_PED_2" en el directorio actual.

## Notas

- Cada archivo de edificio contendrá información sobre su tamaño, ubicación del tornillo y disposición de los pasillos.
- Asegúrate de tener permisos de escritura en el directorio actual para crear la carpeta y archivos.


# Uso del Generador de Edificios

## Descripción

Este script de Python permite generar edificios aleatorios y exportar la información a archivos de texto. Aquí hay un ejemplo simple de cómo utilizarlo.

## Ejemplo de Uso

```python
# Importar las clases Edificio, Exportar y GeneratorArchivo
from tu_archivo_nombre import Edificio, Exportar, GeneratorArchivo

# Crear una instancia de la clase Exportar
edificio_exportador = Exportar()

# Crear una instancia de la clase GeneratorArchivo con la cantidad deseada de archivos (en este caso, 1000)
generador = GeneratorArchivo(cantidad=1000)

# Llamar al método initial del GeneratorArchivo para generar los archivos usando la instancia de Exportar
generador.initial(edificio_exportador)

# Los archivos se generarán en la carpeta "entrada_PED_2" en el directorio actual
# Puedes verificar la carpeta y los archivos generados manualmente
```
---
¡Disfruta del generador de edificios!

---


