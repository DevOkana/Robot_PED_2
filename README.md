Aquí tienes el texto corregido y formateado:


# Proyecto de Gestión de Archivos y Comparación

Este proyecto consta de dos clases principales: `Archivos` y `Comparador`, diseñadas para gestionar la entrada y salida de archivos, así como comparar archivos generados con archivos esperados.

## Clase `Archivos`

### Método `__init__(self, ruta_jar, ruta_carpeta_entrada, ruta_carpeta_salida)`

Inicializa la instancia de la clase Archivos.

Parámetros:
- `ruta_jar`: Ruta del archivo JAR a utilizar.
- `ruta_carpeta_entrada`: Ruta de la carpeta de entrada.
- `ruta_carpeta_salida`: Ruta de la carpeta de salida.

## Clase `Comparador`

### Método `__init__(self, ruta_carpeta_salida_actual, ruta_carpeta_salida_esperada)`

Inicializa la instancia de la clase Comparador.

Parámetros:
- `ruta_carpeta_salida_actual`: Ruta de la carpeta de salida actual.
- `ruta_carpeta_salida_esperada`: Ruta de la carpeta de salida esperada.

# Ejemplo de uso por defecto

Para ejecutar sin agregar ninguna entrada de datos ni salida con este ejemplo podemos iniciar:
- Debemos agregar el archivo JAR generado con nuestro entorno de Java en la ruta actual de este código.
- Ejecutar el `main.py`

```python
from JuegoPrueba import Archivos
from JuegoPrueba import Comparador

if __name__ == "__main__":
    archivo = Archivos() 
    archivo.Gestion_Entrada()
    comparar = Comparador()
    comparar.salida()
```

# Ejemplo de uso pasando rutas

Podemos iniciar la clase `Archivo` con nuestro:
- Primer parámetro de la ruta donde esté el `archivo.jar`.
- El segundo parámetro es la ruta de entrada donde estarán los archivos de entrada `.txt`, por defecto es `entrada_PED_2`.
- El tercer parámetro es la salida donde queremos que se guarden nuestros archivos, por defecto es `salida_actual`, ya que servirá de ayuda para comparar con las salidas esperadas.
### Clase Archivo

```python
def __init__(self, ruta_jar=os.path.join(os.getcwd(), "robot.jar"), ruta_carpeta_entrada=os.path.join(os.getcwd(), "entrada_PED_2"), ruta_carpeta_salida=os.path.join(os.getcwd(), "salida_actual"))
```
- En caso de que modifiquemos la entrada de nuestra salida actual, debemos decirle por parámetro al inicializar el comparador, y el segundo parámetro es con el cual queremos comparar.

### Clase Comparador

```python
def __init__(self, ruta_carpeta_salida_actual=os.path.join(os.getcwd(), "salida_actual"), ruta_carpeta_salida_esperada=os.path.join(os.getcwd(), "salida_esperada")):
```

# Nota
- Tener en cuenta de que los datos de la `salida_esperada` son con los datos de entradas de que hay inicialmente en la carpeta `entrada_PED_2`
- En caso de querer generar otras entradas lo puede hacer con el script que esta en la carpeta de `Tool_Generador_Edificio`