import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QHBoxLayout, QApplication, QPushButton, QLineEdit, \
    QFormLayout, QDialog, QVBoxLayout
from cliente import Cliente

class Ventana1(QMainWindow):
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)
        self.setWindowTitle("Formulario de registro")
        self.setWindowIcon(QIcon('imagenes/icon-clase9.jpg'))

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
        self.horizontal.setContentsMargins(30, 30, 30, 30)

        # ------------ LAYOUT IZQUIERDO-------
        self.ladoIzquierdo = QFormLayout()

        self.letrero1 = QLabel()
        self.letrero1.setText("Informacion del cliente")
        self.letrero1.setFont(QFont("Georgia", 20))
        self.letrero1.setStyleSheet("color: #000080;")
        self.ladoIzquierdo.addRow(self.letrero1)

        self.letrero2 = QLabel()
        self.letrero2.setWordWrap(True)
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nel formulario de abajo. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")
        self.letrero2.setFont(QFont("Georgia", 10))
        self.letrero2.setStyleSheet("color: #000080;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")
        self.ladoIzquierdo.addRow(self.letrero2)

        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Nombre Completo*", self.nombreCompleto)

        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Password*", self.password)

        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)
        self.ladoIzquierdo.addRow("Confirmar Password*", self.password2)

        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        self.botonRegistrar = QPushButton("Registrar")
        self.botonRegistrar.setFixedWidth(90)
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")
        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Boton para limpiar los datos
        self.botonLimpiar = QPushButton("Limpiar")
        self.botonLimpiar.setFixedWidth(90)
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                        "color: #FFFFFF;"
                                        "padding: 10px;"
                                        "margin-top: 40px;")
        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los botones al Layout ladoizquierdo
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)

        # agregamos el layout ladoizquierdo al layout horizontal
        self.horizontal.addLayout(self.ladoIzquierdo)

        # -------OJO IMPORTANTE PONER AL FINAL--------
        self.fondo.setLayout(self.horizontal)

        # -----------LAYOUT DERECHO-------
        self.ladoDerecho = QFormLayout()
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        self.letrero3 = QLabel()
        self.letrero3.setText("Recuperar Contraseña")
        self.letrero3.setFont(QFont("Georgia", 20))
        self.letrero3.setStyleSheet("color: #000080;")
        self.ladoDerecho.addRow(self.letrero3)

        self.letrero4 = QLabel()
        self.letrero4.setFixedWidth(400)
        self.letrero4.setText("Por favor ingrese la informacion para recuperar"
                              "\nla contraseña. Los campos marcados"
                              "\ncon asteriscos son obligatorios.")

        self.letrero4.setFont(QFont("Andale mono", 10))

        self.letrero4.setStyleSheet("color: #000080; margin-botton: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # 1 Prregunta y respuesta
        self.ladoDerecho.addRow(self.letrero4)

        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        self.ladoDerecho.addRow(self.labelPregunta1)

        self.pregunta1 = QLineEdit()

        self.pregunta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta1)

        self.labelRespuesta1 = QLabel("Respuesta de verificaion 1*")

        self.ladoDerecho.addRow(self.labelRespuesta1)

        self.respuesta1 = QLineEdit()

        self.respuesta1.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta1)

        # 2 Prregunta y respuesta

        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        self.ladoDerecho.addRow(self.labelPregunta2)

        self.pregunta2 = QLineEdit()

        self.pregunta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta2)

        self.labelRespuesta2 = QLabel("Respuesta de verificaion 2*")

        self.ladoDerecho.addRow(self.labelRespuesta2)

        self.respuesta2 = QLineEdit()

        self.respuesta2.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta2)

        # 3 Prregunta y respuesta

        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        self.ladoDerecho.addRow(self.labelPregunta3)

        self.pregunta3 = QLineEdit()

        self.pregunta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.pregunta3)

        self.labelRespuesta3 = QLabel("Respuesta de verificaion 3*")

        self.ladoDerecho.addRow(self.labelRespuesta3)

        self.respuesta3 = QLineEdit()

        self.respuesta3.setFixedWidth(320)

        self.ladoDerecho.addRow(self.respuesta3)

        self.botonBuscar = QPushButton("Buscar")

        self.botonBuscar.setFixedWidth(90)

        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 40px;"
                                       )
        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        self.botonRecuperar = QPushButton("Recuperar")

        self.botonRecuperar.setFixedWidth(90)

        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;"
                                          )
        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)
        # Agregamos los botones del Layout ladoDerecho
        self.ladoDerecho.addRow(self.botonRecuperar, self.botonBuscar)

        self.horizontal.addLayout(self.ladoDerecho)

        # -------OJO IMPORTANTE PONER AL FINAL--------
        self.fondo.setLayout(self.horizontal)

        self.ventanaDialogo = QDialog(self)

        self.ventanaDialogo.resize(300, 150)
        self.botonAceptar = QPushButton("Aceptar")
        self.botonAceptar.clicked.connect(self.ventanaDialogo.accept)

        self.ventanaDialogo.setWindowTitle("Formulario de registro")
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        self.mensaje = QLabel('')
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        self.vertical = QVBoxLayout()
        self.vertical.addWidget(self.mensaje)
        self.vertical.addWidget(self.botonAceptar)

        self.ventanaDialogo.setLayout(self.vertical)


    def accion_botonLimpiar(self):
        self.nombreCompleto.clear()
        self.usuario.clear()
        self.password.clear()
        self.password2.clear()
        self.documento.clear()
        self.correo.clear()
        self.pregunta1.clear()
        self.respuesta1.clear()
        self.pregunta2.clear()
        self.respuesta2.clear()
        self.pregunta3.clear()
        self.respuesta3.clear()

    def accion_botonRegistrar(self):

        self.datosCorrectos = True

        if self.password.text() != self.password2.text():
            self.datosCorrectos = False
            self.mensaje.setText("Las contraseñas no coinciden")
            self.ventanaDialogo.exec_()

        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datosCorrectos = False
            self.mensaje.setText("Debes ingresar todos los campos")
            self.ventanaDialogo.exec_()

        if self.datosCorrectos:
            with open('datos/clientes.txt', 'a', encoding='UTF-8') as file:
                file.write(
                    f"{self.nombreCompleto.text()};"
                    f"{self.usuario.text()};"
                    f"{self.password.text()};"
                    f"{self.password2.text()};"
                    f"{self.documento.text()};"
                    f"{self.correo.text()};"
                    f"{self.pregunta1.text()};"
                    f"{self.respuesta1.text()};"
                    f"{self.pregunta2.text()};"
                    f"{self.respuesta2.text()};"
                    f"{self.pregunta3.text()};"
                    f"{self.respuesta3.text()}\n"
                )

            with open('datos/clientes.txt', 'r', encoding='UTF-8') as file:
                for linea in file:
                    print(linea.strip())
        
    #Metodo para hacer el boton buscar
    def accion_botonBuscar(self):

        self.datosCorrectos = True
        
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validacion")

        if (
            self.documento.text() == ''
        ):
            self.datosCorrectos = False

            #Escribimos el texto explicativo
            self.mensaje.setText("Si va a buscar las preguntas"
                                 " para recuperar la contraseña."
                                 "\nDebe primero, ingresa el documento")
            #Hacemos que la ventana dialogo se vea
            self.ventanaDialogo.exec_()
        if (not self.documento.text().isnumeric()):
            self.datosCorrectos = False
            # texto explicativo del error
            self.mensaje.setText("El documento ingresado no es numerico"
                                 "\nNo ingrese letras ni caracteres especiales.")
            self.ventanaDialogo.exec_()
            # limpiamos el campo del documento
            self.documento.setText('')

        if (self.datosCorrectos):
            # abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            # creamos una lista vacia para guardar todos los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')

                # obtenemos del string una lista de 11 datos separados por ;
                lista = linea.split(";")
                # para pausar si ya no hay mas registros en el archivo
                if linea == '':
                    break

                # creamos un objeto tipo cliente llamado u
                u = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7],
                                lista[8], lista[9], lista[10], )

                # metemos el objeto en la lista de usuarios
                usuarios.append(u)

            self.file.close()

            # ya tenemos  la lisata de usuarios con todos los usuarios
            existeDocumento = False

            # buscamos en la lista usuario por usuario si exsiste el documento
            for u in usuarios:
                # comparamos el documento ingresado
                # si corresponde con el documento es el usuario corecto
                if u.documento == self.documento.text():
                    # mostramos las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)
                    # indicamos que se encotro el documento
                    existeDocumento = True
                    break
            # validamos si no existe un usuario con ese documento
            if (
                    not existeDocumento
            ):
               # texto explicativo del error
                self.mensaje.setText("No existe un usuario con ese documento:\n"
                                             + self.documento.text())
                self.ventanaDialogo.exec_()

    def accion_botonRecuperar(self):
        self.datosCorrectos = True
        # establecemos el titulo de la ventana emergente
        self.ventanaDialogo.setWindowTitle("Recuperar Contraseña")
        # validamos si se buscaron las preguntas
        if (self.pregunta1.text() == ''
                or self.pregunta2.text() == ''
                or self.pregunta3.text() == ''):
            self.datosCorrectos = False

            # texto explicativo del error
            self.mensaje.setText("Para recuperar la contraseña debe buscar las preguntas de verificacion.\n\n"
                                 "Primero ingrese su documento y luego"
                                 " pulse el boton buscar.")
            self.ventanaDialogo.exec_()
        if (self.pregunta1.text() != '' and
                self.respuesta1.text() == '' and
                self.pregunta2.text() != '' and
                self.respuesta2.text() == '' and
                self.pregunta3.text() != '' and
                self.respuesta3.text() == ''):
            self.datosCorrectos = False

            # texto explicativo del error
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "ingresar las respuestas de cada pregunta.")
            self.ventanaDialogo.exec_()
        # si los datos son correctos
        if (self.datosCorrectos):
            # abrimos el archivo en modo lectura
            self.file = open('datos/clientes.txt', 'rb')

            # lista vacia para guardar los usuarios
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # obtenemos del string una lista de 11 datos separados por ;
                lista = linea.split(";")
                # para parar si no hay mas datos
                if linea == '':
                    break
                # creamos un objeto tipo cliente llamado u
                u = Cliente(lista[0], lista[1], lista[2], lista[3], lista[4], lista[5], lista[6], lista[7],
                            lista[8], lista[9], lista[10], )

                # metemos el objeto en la lista de usuarios
                usuarios.append(u)

            self.file.close()

            # en este punto ya tenemos la lista con los usuarios

            # variable para controlar si existe el documento
            existeDocumento = False

            # dedinimos las variables para guardar las preguntas
            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''

            for u in usuarios:
                # comparamos el documento ingresado
                # si corresponde con el documento, es el ususario correcto
                if u.documento == self.documento.text():
                    # cambiamos la variable a true
                    existeDocumento = True
                    # guardamos las respuestas
                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    passw = u.password
                    # detenemos el malparido for
                    break
                    # verificamos si las respuestas son las correctas
                    # hacemos que las respuestas esten en minuscula
            if (
                    # usamos strip() para borrar espacios y saltos de linea
                    self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                    self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                    self.respuesta3.text().lower().strip() == resp3.lower().strip()
            ):
                # limpiamos los campos
                self.accion_botonLimpiar()
                # escribimos el texto explicativo
                self.mensaje.setText("La contraseña es: " + passw)
                # hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()
            else:
                # escribimos el texto de error
                self.mensaje.setText("Las respuestas son incorrectas")
                self.ventanaDialogo.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana1 = Ventana1()
    ventana1.show()
    sys.exit(app.exec_())


