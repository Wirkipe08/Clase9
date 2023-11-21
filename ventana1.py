import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout, QDialog, QDialogButtonBox,  QVBoxLayout
from PyQt5 import QtGui, QtCore
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


        #-----------LAYOUT DERECHO-------
        self.ladoDerecho = QFormLayout
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText("Recuperar Congtraseña")
        self.letrero3.setFont(QFont("Geordia", 20))
        self.letrero3.setStyleSheet("color: #000080;")
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informacion del cliente"
                              "\nel el formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        self.letrero4.setFont(QFont("Geordia", 20))
        self.letrero4.setStyleSheet("color: #000080;"
                                    "margin-top: 20px;"
                                    "padding-botton: 10px;"
                                    "boder: 2px solid #000080;"
                                    "boder-lef: none;"
                                    "boder-rigth: none;"
                                    "border-top none;")
        self.layoutDerecho.addRow(self.letrero4)

        #-----1
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta1)


        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")
        self.ladoDerecho.addRow(self.pregunta1)

        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        #----2
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta1 = QLabel("Respuesta de verificacion 2*")


        self.respuesta2 = QLineEdit()
        self.respuesta2.setFixedWidth(320)
        self.ladoDerecho.addRow(self.labelPregunta2)

        #-----3
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")



        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")
        self.ladoDerecho.addRow(self.pregunta1)

        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)
        self.ladoDerecho.addRow(self.labelPregunta3)

        #Boton para buscar preguntas
        self.botonBuscar = QPushButton("Buscar")
        self.botonBuscar.setFixedWidth(90)
        self.botonBuscar.setStyleSheet("background-color: #008B45"
                                       "color: #FFFFFF;"
                                       "paddin: 10px"
                                       "margin-top: 40px"
                                       )
        self.botonRecuperar = QPushButton("Recuperar")
        self.botonRecuperar.setFixedWidth(90)
        self.botonRecuperar.setStyleSheet("background-color: #008B45"
                                       "color: #FFFFFF;"
                                       "paddin: 10px"
                                       "margin-top: 40px"
                                       )

        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)




        self.horizontal.addLayout(self.ladoDerecho)

        # -------OJO IMPORTANTE PONER AL FINAL--------
        self.fondo.setLayout(self.horizontal)

    def accion__botonLimpiar(self):
        self.nombreCompleto.setText('')
        self.usuario.setText('')
        self.password.setText('')
        self.password2.setText('')
        self.documento.setText('')
        self.correo.setText('')
        self.pregunta1.setText('')
        self.respuesta1.setText('')
        self.pregunta2.setText('')
        self.respuesta2.setText('')
        self.pregunta3.setText('')
        self.respuesta3.setText('')

    def accion__botonRegistrar(self):

        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowMenuHint | QtCore.Qt.WindowTitleMint)

        self.ventanaDialogo.resize(300, 150)

        self.botonAcepetar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAcepetar)
        self.opciones.accepted.connectec(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.vertical = QVBoxLayout()
        self.mensaje = QLabel('')
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; paddinf: 10px;")

        self.vertical.addWidget(self.mensaje)

        self.vertical.addWidget(self.opciones)

        self.ventanaDialogo.setLayout(self.vertical)
        self.datosCorrectos = True

        if(
            self.password.text() != self.password2.text()
        ):
            self.datosCorrectos = False


            self.mensaje.setText("Los password son iguales")

            self.ventanaDialogo.exec_()

        if(
                self.nombreCompleto.setText('')
                or self.usuario.setText('')
                or self.password.setText('')
                or self.password2.setText('')
                or self.documento.setText('')
                or self.correo.setText('')
                or self.pregunta1.setText('')
                or self.respuesta1.setText('')
                or self.pregunta2.setText('')
                or self.respuesta2.setText('')
                or self.pregunta3.setText('')
                or self.respuesta3.setText('')
        ):
            self.datosCorrectos = False

            self.mensaje.setText("Debes de ingresar todos los campos")
            self.ventanaDialogo.exec_()


        if self.datosCorrectos:

            self.file = open('datos/clientes.txt','ab'')
            self.file.wrate(bytes(
                self.nombreCompleto.setText() + ';'
                + self.usuario.setText() + ';'
                + self.password.setText() + ';'
                + self.password2.setText() + ';'
                + self.documento.setText() + ';'
                + self.correo.setText() + ';'
                + self.pregunta1.setText() + ';'
                + self.respuesta1.setText() + ';'
                + self.pregunta2.setText() + ';'
                + self.respuesta2.setText() + ';'
                + self.pregunta3.setText() + ';'
                + self.respuesta3.setText() + '\n'
                ,encodings='UTF-8'))
            #Cerramos el archivo
            self.file.close()

            #Abrimos en modo lectura en formato bytes
            self.file = open('datos/clientes.txt','rb')
            while self.file:
                linea = self.file.readline().decode('UFT-8')
                print(linea)
                if linea == '':
                    break
            self.file.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())


