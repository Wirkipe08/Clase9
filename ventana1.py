import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication
from PyQt5 import QtGui
import sys
class Ventana1(QMainWindow):
    def __init__(self,parent=None):
        super(Ventana1,self).__init__(parent)
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QtGui.QIcon('imagenes/icon-clase9.jpg'))

        self.ancho = 900
        self.alto = 600

        self.resize(self.ancho, self.alto)
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.fondo = QLabel(self)

        self.imagenFondo = QPixmap('imagenes/paris-fondo.jpeg')
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())
        self.setCentralWidget(self.fondo)

        self.horizontal = QHBoxLayout()

        self.horizontal.setContentsMargins(30,30,30,30)


        #-------OJO IMPORTANTE PONER AL FINAL--------
        self.fondo.setLayout(self.horizontal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())


