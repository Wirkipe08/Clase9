import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout
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

        # ------------ LAYOUT IZQUIERDO-------
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Informacion del cliente")
        self.letrero1.setFont(QFont("Georgia", 20))
        self.letrero1.setStyleSheet("color: #000080;")
        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setFixedWidth(340)
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nel el formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")
        self.letrero2.setFont(QFont("Georgia", 10))
        self.letrero2.setStyleSheet("color: #000080;"
                                    "margin-top: 20px;"
                                    "padding-botton: 10px;"
                                    "boder: 2px solid #000080;"
                                    "boder-lef: none;"
                                    "boder-rigth: none;"
                                    "border-top none;")
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usario = QLineEdit()
        self.usario.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Usuario*", self.usario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        self.ladoIzquierdo.addRow("Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit
        self.correo.setFixedWidth(250)

        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")

        self.botonRegistrar.setFixedWidth(90)

        self.botonRegistrar.setStyleSheet("background-color: #0008845;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")

        self.botonLimpiar.setFixedWidth(90)

        self.botonLimpiar.setStyleSheet("background-color: #0008845;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los botones al Layout ladoizquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # agregamos el layout ladoizquierdo al layou horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        #-------OJO IMPORTANTE PONER AL FINAL--------
        self.fondo.setLayout(self.horizontal)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())


