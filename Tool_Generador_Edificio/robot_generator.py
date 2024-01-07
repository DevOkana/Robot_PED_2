import os
import random

# Clase para representar un edificio con pasillos, tornillos, etc.
class Edificio:
    def __init__(self):
        #Inicialización de atributos
        self.filas_aleatorias = random.randint(3, 20)
        self.columnas_aleatorias = random.randint(3, 20)
        self.espacio_reducido = 'E'
        self.paso_libre = 'L'
        self.tornillo = 'T'

    #Generación de la Matriz que representa el edificio
    def GeneradorEdificio(self):
        # Crear una matriz de filas_aleatorias x columnas_aleatorias con pasillos libres inicialmente
        edificio = [[self.espacio_reducido for _ in range(self.columnas_aleatorias)] for _ in
                    range(self.filas_aleatorias)]

        # Colocar el tornillo en una posición aleatoria
        fila_tornillo = random.randint(0, self.filas_aleatorias - 1)
        columna_tornillo = random.randint(0, self.columnas_aleatorias - 1)
        edificio[fila_tornillo][columna_tornillo] = self.tornillo

        #Recogeremos las fila hasta llegar a donde esta el tornillo poniendo L
        for fila in range(fila_tornillo):
            edificio[fila][columna_tornillo-1] = self.paso_libre

        # Recogeremos las columnas hasta llegar a donde esta el tornillo poniendo L
        for columna in range(columna_tornillo):
            edificio[0][columna] = self.paso_libre

        #Si la fila del tornillo es mayor que 0 agrega un L en una columna inferior columna_tornillo-1
        if (fila_tornillo > 0):
            edificio[fila_tornillo][columna_tornillo-1] = self.paso_libre
        return edificio


# Clase para exportar información del edificio a archivos de texto
class Exportar:
    count = 0  # Contador compartido

    def __init__(self, nombre_archivo="", ruta=os.getcwd()):
        Exportar.count += 1
        if nombre_archivo == "":
            self.nombre_archivo = f"entrada{Exportar.count}.txt"
        else:
            self.nombre_archivo = nombre_archivo
        self.ruta_carpeta = os.path.join(ruta, "../entrada_PED_2")#Ruta donde se encuentra la entrada de los txt
        self.ruta_actual = os.path.join(self.ruta_carpeta, self.nombre_archivo)

    #Verifica que el archiv este en la ruta_actual
    def Verificar(self):
        return os.path.exists(self.ruta_actual)

    #Crea la carpeta en caso de que no este
    def CrearCarpeta(self):
        if not os.path.exists(self.ruta_carpeta):
            os.makedirs(self.ruta_carpeta)

    #Escribe en .txt los datos del edificio generado
    def Read_and_Write(self):
        mi_edificio = Edificio()
        edificio = mi_edificio.GeneradorEdificio()

        self.CrearCarpeta()

        if self.Verificar():
            print(f"El archivo {self.ruta_actual} ya existe.")
        else:
            with open(self.ruta_actual, 'w') as archivo:
                archivo.write(str(mi_edificio.filas_aleatorias) + '\n')
                archivo.write(str(mi_edificio.columnas_aleatorias) + '\n')
                # Imprimir el edificio
                for fila in edificio:
                    archivo.write(' '.join(fila) + '\n')


# Clase para generar múltiples archivos de edificios
class GeneratorArchivo:
    def __init__(self,cantidad):
        self.count = 0  # Inicializar el contador de archivos
        self.cantidad = cantidad
    def initial(self, edificio_exportador):
        x = 0
        while x < self.cantidad:

            edificio_exportador.Read_and_Write()
            x += 1


# Uso del GeneratorArchivo para generar 1000 archivo
edificio_exportador = Exportar()
generador = GeneratorArchivo(1000)
generador.initial(edificio_exportador)
