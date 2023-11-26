import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication
from PyQt5 import QtGui

class Ventana2(QMainWindow):

    # Metodo constructor de la ventana
    def __init__(self, parent=None):
        super(Ventana2, self).__init__(parent)

        # poner el titulo
        self.setWindowTitle("Usuarios Registrados")
        #Ponemos un icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icon-clase9.jpg'))

        # Establecemos las propiedades de ancho por alto
        self.ancho = 900
        self.alto = 600

        # Establecemos el tamaño de la venata
        self.resize(self.ancho, self.alto)

        # Centrar la ventana en la pantalla
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el tamaño de la ventana para evitar cambiarlo
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.fondo = QLabel(self)

        self.imagenFondo = QPixmap('imagenes/espacio-fondo.jpeg')
        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)
        # Hacemos que se adapte al tamaño de la imagen
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        # Establecemos la ventana de fondo como ventana central
        self.setCentralWidget(self.fondo)

        # distribucion de los elementos
        self.vertical = QVBoxLayout()










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana2 = Ventana2()
    ventana2.show()
    sys.exit(app.exec_())

