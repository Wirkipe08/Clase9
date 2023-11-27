import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QScrollArea, QTableWidget, \
    QTableWidgetItem, QPushButton, QApplication
from PyQt5 import QtGui

from cliente import Cliente


class Ventana3(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self, parent=None):
        super(Ventana3, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Forma Tabular")

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
        self.imagenFondo = QPixmap('imagenes/noparis-fondo.jpeg')
        # Establecemos la imagen de fondo
        self.fondo.setPixmap(self.imagenFondo)
        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        self.file = open('datos/clientes.txt', 'rb')
        # lista vacia para guardar los usuarios
        usuarios = []

        while self.file:
            linea = self.file.readline().decode('UTF-8')

            # obtenemos del string una lista de 11 datos separados por ;
            lista = linea.split(";")
            # para pausar si ya no hay mas registros en el archivo
            if linea == '':
                break

            # creamos un objeto tipo cliente llamado u
            u = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7], lista[8],
                        lista[9], lista[10], )

            # metemos el objeto en la lista de usuarios
            usuarios.append(u)

        self.file.close()

        # obtenemos el numero de usuarios registrados
        self.numeroUsuarios = len(usuarios)

        # variable contadora para controlar los usuarios en la lista usuarios
        self.contador = 0

        self.vertical = QVBoxLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Usuarios registrados")
        self.letrero1.setFont(QFont("Times New Roman", 20))
        self.letrero1.setStyleSheet('color: #EFEFEF')
        self.vertical.addWidget(self.letrero1)
        self.vertical.addStretch()

        # creamos un scroll
        self.scrollArea = QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        # tabla = tuHermana
        # creamos una tabla, como la hermana de quien este leyendo esto si es que se robo el codigo
        self.tabla = QTableWidget()

        # definimos el numero de columnas que tendra la tabla
        self.tabla.setColumnCount(11)

        # definimos el ancho de cada columna
        self.tabla.setColumnWidth(0, 200)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 150)
        self.tabla.setColumnWidth(3, 150)
        self.tabla.setColumnWidth(4, 200)
        self.tabla.setColumnWidth(5, 150)
        self.tabla.setColumnWidth(6, 150)
        self.tabla.setColumnWidth(7, 150)
        self.tabla.setColumnWidth(8, 150)
        self.tabla.setColumnWidth(9, 150)
        self.tabla.setColumnWidth(10, 150)

        # definimos el texto de la cabecera
        self.tabla.setHorizontalHeaderLabels(['Nombre',
                                              'Usuario',
                                              'Password',
                                              'Documento',
                                              'Correo',
                                              'Pregunta 1',
                                              'Respuesta 1',
                                              'Pregunta 2 ',
                                              'Respuesta 2',
                                              'Pregunta 3',
                                              'Respuesta 3'])

        # establecemos el numero de filas
        self.tabla.setRowCount(self.numeroUsuarios)

        # Llenamos la tabla


        for u in usuarios:
            self.tabla.setItem(self.contador, 0, QTableWidgetItem(u.nombreCompleto))
            self.tabla.setItem(self.contador, 1, QTableWidgetItem(u.usuario))
            self.tabla.setItem(self.contador, 2, QTableWidgetItem(u.password))
            self.tabla.setItem(self.contador, 3, QTableWidgetItem(u.documento))
            self.tabla.setItem(self.contador, 4, QTableWidgetItem(u.correo))
            self.tabla.setItem(self.contador, 5, QTableWidgetItem(u.pregunta1))
            self.tabla.setItem(self.contador, 6, QTableWidgetItem(u.respuesta1))
            self.tabla.setItem(self.contador, 7, QTableWidgetItem(u.pregunta2))
            self.tabla.setItem(self.contador, 8, QTableWidgetItem(u.respuesta2))
            self.tabla.setItem(self.contador, 9, QTableWidgetItem(u.pregunta3))
            self.tabla.setItem(self.contador, 10, QTableWidgetItem(u.respuesta3))
            self.contador += 1

        # metemos la tabla en el scroll
        self.scrollArea.setWidget(self.tabla)
        # metemos el layout vertical en el scroll
        self.vertical.addWidget(self.scrollArea)

        self.vertical.addStretch()

        # Hacemos el boton para continuar
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

        # poner al final
        self.fondo.setLayout(self.vertical)

    def accion_botonVolver(self):
        from ventana2 import Ventana2
        self.hide()
        self.ventana2 = Ventana2()
        self.ventana2.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana3 = Ventana3()
    ventana3.show()
    sys.exit(app.exec_())