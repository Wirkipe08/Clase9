import math
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton

from cliente import Cliente

class Ventana2(QMainWindow):
    # Método constructor de la ventana
    def __init__(self, parent=None):
        super(Ventana2, self).__init__(parent)

        # Poner el titulo
        self.setWindowTitle("Usuarios Registrados")

        # Ponemos el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icon-clase9.jpg'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la ventana
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)
        # Definimos la imagen de fondo
        self.imagenFondo = QPixmap('imagenes/noche-fondo.jpg')
        # Establecemos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)
        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # Distribucion de los elementos
        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Ver los usuarios registrados")
        self.letrero1.setFont(QFont("Times New Roman", 20))
        self.letrero1.setStyleSheet('color: #EFEFEF')
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # Creamos un scroll
        self.scrollArea = QScrollArea()
        self.scrollArea.setStyleSheet('background-color: transparent;')
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda
        self.contenedora = QWidget()
        # Creamos un layout de grid para poner la cuadrícula de elementos
        self.cuadricula = QGridLayout(self.contenedora)
        # Metemos la cuadrícula en el scroll
        self.scrollArea.setWidget(self.contenedora)
        # Metemos el layout vertical en el scroll
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en modo lectura
        self.file = open('datos/clientes.txt', 'rb')
        # Creamos una lista vacía para guardar todos los usuarios
        usuarios = []

        while True:
            linea = self.file.readline().decode('UTF-8')

            # Obtenemos del string una lista de 11 datos separados por ;
            lista = linea.split(";")
            if not linea:
                break

            # Creamos un objeto tipo cliente llamado u
            u = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                        lista[9], lista[10])

            # Metemos el objeto en la lista de usuarios
            usuarios.append(u)

        self.file.close()

        # Obtenemos el numero de usuarios registrados
        self.numeroUsuarios = len(usuarios)

        # Variable contadora para controlar los usuarios en la lista usuarios
        self.contador = 0

        # Definimos la cantidad de elementos por columna
        self.elementosPorColumna = 3

        # Calculamos el numero de filas
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # Controlamos los botones por una variable
        self.botones = QButtonGroup()

        # Definimos que el controlador de los botones debe agrupar a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna + 1):

                # Validamos que se ingrese la cantidad de usuarios correctos
                if self.contador < self.numeroUsuarios:
                    # En cada celda de la cuadrícula va una ventana
                    self.ventanaAuxiliar = QWidget()
                    # Determinamos el ancho y el alto
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Creamos un layout vertical para cada cuadrícula
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un botón por cada usuario mostrando su cédula
                    self.botonAccion = QPushButton(usuarios[self.contador].documento)
                    # Ponemos el ancho
                    self.botonAccion.setFixedWidth(150)
                    # Ponemos estilo
                    self.botonAccion.setStyleSheet("background-color: #EFEFEF;"
                                                   "color: black;"
                                                   "padding: 10px")
                    # Metemos el botón en el layout vertical para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el botón al grupo con su cédula como id
                    self.botones.addButton(self.botonAccion, self.contador)

                    self.verticalCuadricula.addStretch()

                    # A la ventana le asignamos el layout vertical
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la cuadrícula le agregamos la ventana en la fila y columna actual
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        # Establecemos el método para que funcionen todos los botones
        self.botones.buttonClicked[int].connect(self.metodo_accionBotones)

        # Hacemos el boton para continuar
        self.botonFormaTabular = QPushButton("Forma Tabular")
        # Establecemos el ancho del boton
        self.botonFormaTabular.setFixedWidth(100)
        # Le ponemos los estilos
        self.botonFormaTabular.setStyleSheet("background-color: #008845;"
                                             "color: #FFFFFF;"
                                             "padding: 10px;"
                                             "margin-top: 10px;")

        self.botonFormaTabular.clicked.connect(self.accion_botonFormaTabular)
        # Agregamos los dos botones al layout ladoIzquierdo
        self.vertical.addWidget(self.botonFormaTabular)

        # Hacemos el boton para volver
        self.botonVolver = QPushButton("Volver")
        # Establecemos el ancho del boton
        self.botonVolver.setFixedWidth(100)
        # Le ponemos los estilos
        self.botonVolver.setStyleSheet("background-color: #008845;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        self.botonVolver.clicked.connect(self.accion_botonVolver)

        # Agregamos el boton
        self.vertical.addWidget(self.botonVolver)



        # Poner siempre al final
        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, usuario_id):
        print(usuario_id)

    def accion_botonVolver(self):
        from ventana1 import Ventana1
        self.hide()
        self.ventana1 = Ventana1()
        self.ventana1.show()

    def accion_botonFormaTabular(self):
        from ventana3 import Ventana3
        self.hide()
        self.ventana3 = Ventana3()
        self.ventana3.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())





