import os
import subprocess
import filecmp
from natsort import natsorted

class Archivos:
    def __init__(self, ruta_jar=os.path.join(os.getcwd(), "robot.jar"), ruta_carpeta_entrada=os.path.join(os.getcwd(), "entrada_PED_2"), ruta_carpeta_salida=os.path.join(os.getcwd(), "salida_actual")):
        """
        Inicializa la instancia de la clase Archivos.

        Parámetros:
        - ruta_jar: Ruta del archivo JAR a utilizar.
        - ruta_carpeta_entrada: Ruta de la carpeta de entrada.
        - ruta_carpeta_salida: Ruta de la carpeta de salida.
        """
        self.ruta_jar = ruta_jar
        self.ruta_carpeta_entrada = ruta_carpeta_entrada
        self.ruta_carpeta_salida = ruta_carpeta_salida


    def Gestion_Entrada(self):
        """
        Gestiona la entrada de archivos en la carpeta especificada.
        Itera sobre los archivos de la carpeta de entrada e inicia el proceso para cada uno.
        """
        entrada = natsorted(os.listdir(self.ruta_carpeta_entrada))

        count = 1
        for archivo in entrada:
            ruta_completa = os.path.join(self.ruta_carpeta_entrada,archivo)
            #print(ruta_completa)
            self.iniciar(ruta_completa,self.Gestion_Salida(count))
            count += 1


    def Gestion_Salida(self, cantidad):
        """
        Gestiona la salida de archivos en la carpeta especificada.
        Crea un archivo de salida con un nombre único basado en la cantidad proporcionada.

        Parámetros:
        - cantidad: Número único para generar el nombre del archivo de salida.

        Retorna:
        - Ruta completa del archivo de salida.
        """
        # Verificar si la carpeta de salida existe, si no, crearla
        if not os.path.exists(self.ruta_carpeta_salida):
            os.makedirs(self.ruta_carpeta_salida)
        nombre_archivo = f"salida{cantidad}.txt"
        ruta_completa = os.path.join(self.ruta_carpeta_salida, nombre_archivo)

        if not os.path.exists(ruta_completa):
            # Si el archivo no existe, crearlo
            with open(ruta_completa, 'w') as archivo:
                archivo.write("")

        return ruta_completa

    def iniciar(self, entrada, salida):
        """
        Inicia el proceso para un archivo de entrada, generando un archivo de salida.

        Parámetros:
        - entrada: Ruta del archivo de entrada.
        - salida: Ruta del archivo de salida.
        """
        comando  = ["java", "-jar", self.ruta_jar, entrada, salida]
        subprocess.run(comando)

class Comparador:
    def __init__(self, ruta_carpeta_salida_actual=os.path.join(os.getcwd(), "salida_actual"), ruta_carpeta_salida_esperada=os.path.join(os.getcwd(), "salida_esperada")):
        """
        Inicializa la instancia de la clase Comparador.

        Parámetros:
        - ruta_carpeta_salida_actual: Ruta de la carpeta de salida actual.
        - ruta_carpeta_salida_esperada: Ruta de la carpeta de salida esperada.
        """
        self.ruta_carpeta_salida_actual = ruta_carpeta_salida_actual
        self.ruta_carpeta_salida_esperada = ruta_carpeta_salida_esperada
        self.archivos_iguales = []
        self.archivos_diferentes = []

    def salida(self, ruta_actual=None, ruta_esperada=None):
        """
        Compara los archivos de las carpetas de salida actual y esperada, identificando archivos iguales y diferentes.

        Parámetros:
        - ruta_actual: Ruta de la carpeta de salida actual.
        - ruta_esperada: Ruta de la carpeta de salida esperada.
          (Ambos parámetros son opcionales y utilizan las rutas predeterminadas si no se proporcionan.)
        """
        # Establecer valores predeterminados dentro del cuerpo del método
        if ruta_actual is None:
            ruta_actual = self.ruta_carpeta_salida_actual
        if ruta_esperada is None:
            ruta_esperada = self.ruta_carpeta_salida_esperada

        salida_actual = os.listdir(ruta_actual)
        salida_esperada = os.listdir(ruta_esperada)

        for archivo_actual in salida_actual:
            ruta_completa_actual = os.path.join(self.ruta_carpeta_salida_actual, archivo_actual)
            archivo_esperado = os.path.join(self.ruta_carpeta_salida_esperada, archivo_actual)

            if archivo_actual in salida_esperada:
                if self.son_archivos_iguales(ruta_completa_actual, archivo_esperado):
                    self.archivos_iguales.append(archivo_actual)
                else:
                    self.archivos_diferentes.append(archivo_actual)
            else:
                self.archivos_diferentes.append(archivo_actual)

        for archivo_esperado in salida_esperada:
            if archivo_esperado not in salida_actual:
                self.archivos_diferentes.append(archivo_esperado)

        self.imprimir_resumen()

    def son_archivos_iguales(self, archivo1, archivo2):
        """
        Verifica si dos archivos son iguales utilizando filecmp.

        Parámetros:
        - archivo1: Ruta del primer archivo a comparar.
        - archivo2: Ruta del segundo archivo a comparar.

        Retorna:
        - True si los archivos son iguales, False de lo contrario.
        """
        return filecmp.cmp(archivo1, archivo2)

    def imprimir_resumen(self):
        """
        Imprime un resumen de la comparación de archivos.
        Muestra la cantidad de archivos iguales y diferentes, así como una lista de archivos diferentes si los hay.
        """
        print("Resumen:")
        print(f"Archivos iguales: {len(self.archivos_iguales)}")
        print(f"Archivos diferentes: {len(self.archivos_diferentes)}")
        if len(self.archivos_diferentes) > 0:
            for archivo in self.archivos_diferentes:
                print(f"- {archivo}")
