# Diseñado por Facundo Padilla - https://www.github.com/facundopadilla
# Éste contenido es de uso libre y contiene licencia MIT, por lo tanto, no me responsabilizo de daños y prejuicios en el caso de su uso y/o modificación.
# @author: facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui_tateti import Ui_MainWindow 
import sys

class Tateti(QtWidgets.QMainWindow):

	# -- Constructor --

    def __init__(self):

        super(Tateti, self).__init__() # inicializo y heredo los widgets

        self.tateti = Ui_MainWindow() # creo mi atributo

        self.tateti.setupUi(self) # cargo mi setupUi

        # -- Variables --

        self.turno = 1 # si vale 1, es del jugador 1, si es 2, es del jugador 2, pero siempre empieza el jugador 1
        self.matriz = [[None, None, None],[None, None, None],[None, None, None]] # matriz de 3x3
        self.contador = 0 # para verificar si hay empate o no

        # --- Clicked buttons ---

            # >>> Matriz de Tateti <<<

        self.tateti.btn1.clicked.connect(self.btn1Clicked) # cuando hago click en el boton 1 (fila 1, columna 1)
        self.tateti.btn2.clicked.connect(self.btn2Clicked) # cuando hago click en el boton 2 (fila 1, columna 2)
        self.tateti.btn3.clicked.connect(self.btn3Clicked) # cuando hago click en el boton 3 (fila 1, columna 3)
        self.tateti.btn4.clicked.connect(self.btn4Clicked) # cuando hago click en el boton 4 (fila 2, columna 1)
        self.tateti.btn5.clicked.connect(self.btn5Clicked) # cuando hago click en el boton 5 (fila 2, columna 2)
        self.tateti.btn6.clicked.connect(self.btn6Clicked) # cuando hago click en el boton 6 (fila 2, columna 3)
        self.tateti.btn7.clicked.connect(self.btn7Clicked) # cuando hago click en el boton 7 (fila 3, columna 1)
        self.tateti.btn8.clicked.connect(self.btn8Clicked) # cuando hago click en el boton 8 (fila 3, columna 2)
        self.tateti.btn9.clicked.connect(self.btn9Clicked) # cuando hago click en el boton 9 (fila 3, columna 3)

            # >>> Boton de "Comenzar juego" <<<

        self.tateti.btnComenzar.clicked.connect(self.comenzar)

    # --- Funciones ---

    def comenzar(self):

        # -- Limpiar las X y O --
        self.tateti.btn1.setText("")
        self.tateti.btn2.setText("")
        self.tateti.btn3.setText("")
        self.tateti.btn4.setText("")
        self.tateti.btn5.setText("")
        self.tateti.btn6.setText("")
        self.tateti.btn7.setText("")
        self.tateti.btn8.setText("")
        self.tateti.btn9.setText("")

        # -- Limpiar matriz --
        self.matriz = [[None, None, None],[None, None, None],[None, None, None]]

        # -- Activar casillas --
        self.tateti.btn1.setEnabled(True)
        self.tateti.btn2.setEnabled(True) 
        self.tateti.btn3.setEnabled(True) 
        self.tateti.btn4.setEnabled(True) 
        self.tateti.btn5.setEnabled(True) 
        self.tateti.btn6.setEnabled(True) 
        self.tateti.btn7.setEnabled(True) 
        self.tateti.btn8.setEnabled(True) 
        self.tateti.btn9.setEnabled(True) 

        # --- Reiniciar el contador ---
        self.contador = 0


    def validarGanador(self):

        # --- Filas y columnas en X ---
        if((self.matriz[0][0] == "x" and self.matriz[0][1] == "x" and self.matriz[0][2] == "x") # fila 1 completa de X
        or (self.matriz[1][0] == "x" and self.matriz[1][1] == "x" and self.matriz[1][2] == "x") # fila 2 completa de X
        or (self.matriz[2][0] == "x" and self.matriz[2][1] == "x" and self.matriz[2][2] == "x") # fila 3 completa de X
        or (self.matriz[0][0] == "x" and self.matriz[1][0] == "x" and self.matriz[2][0] == "x") # columna 1 completa de X
        or (self.matriz[0][1] == "x" and self.matriz[1][1] == "x" and self.matriz[2][1] == "x") # columna 2 completa de X
        or (self.matriz[0][2] == "x" and self.matriz[1][2] == "x" and self.matriz[2][2] == "x") # columna 3 completa de X
        or (self.matriz[0][0] == "x" and self.matriz[1][1] == "x" and self.matriz[2][2] == "x") # diagonal de izquierda a derecha de X
        or (self.matriz[0][2] == "x" and self.matriz[1][1] == "x" and self.matriz[2][0] == "x")): # diagonal de derecha a izquierda de X
            self.ganador("Ganador: jugador 1") # envío el ganador

        # -- Filas y columnas en O ---
        elif((self.matriz[0][0] == "o" and self.matriz[0][1] == "o" and self.matriz[0][2] == "o") # fila 1 completa de O
        or (self.matriz[1][0] == "o" and self.matriz[1][1] == "o" and self.matriz[1][2] == "o") # fila 2 completa de O
        or (self.matriz[2][0] == "o" and self.matriz[2][1] == "o" and self.matriz[2][2] == "o") # fila 3 completa de O
        or (self.matriz[0][0] == "o" and self.matriz[1][0] == "o" and self.matriz[2][0] == "o") # columna 1 completa de O
        or (self.matriz[0][1] == "o" and self.matriz[1][1] == "o" and self.matriz[2][1] == "o") # columna 2 completa de O
        or (self.matriz[0][2] == "o" and self.matriz[1][2] == "o" and self.matriz[2][2] == "o") # clumna 3 completa de O
        or (self.matriz[0][0] == "o" and self.matriz[1][1] == "o" and self.matriz[2][2] == "o") # diagonal de izquierda a derecha de O
        or (self.matriz[0][2] == "o" and self.matriz[1][1] == "o" and self.matriz[2][0] == "o")): # diagonal de derecha a izquierda de O
            self.ganador("Ganador: jugador 2") # envío el ganador

        # -- Si nadie gana --
        elif self.contador == 9:
            self.ganador("Empate, nadie gana.")

    def ganador(self, ganador):
        alerta = QMessageBox() # creo una caja de mensaje (QMessageBox)
        alerta.setWindowTitle("Ganador") # le defino un título
        alerta.setText(f"{ganador}") # le indico quien es el ganador
        mostrar_alerta = alerta.exec_() # la ejecuto y muestro en pantalla

    def btn1Clicked(self):
        if self.turno == 1: # si es el turno del primer jugador
            self.tateti.btn1.setText("X") # le modifico el texto del botón por una X
            self.matriz[0][0] = "x" # añado a la matriz la X
            self.turno = 2 # modifico el turno y ahora es del jugador 2
        elif self.turno == 2: # si es el turno del segundo jugador
            self.tateti.btn1.setText("O") # le modifico el texto del botón por una O
            self.turno = 1 # modifico el turno y ahora es del jugador 1
            self.matriz[0][0] = "o" # añado a la matriz la X
        self.tateti.btn1.setEnabled(False) # desactivo para que no haya modificación
        self.contador += 1 # sumo el contador
        self.validarGanador() # valido si ganó o no

    def btn2Clicked(self):
        if self.turno == 1:
            self.tateti.btn2.setText("X")
            self.matriz[0][1] = "x" 
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn2.setText("O")
            self.matriz[0][1] = "o" 
            self.turno = 1
        self.tateti.btn2.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn3Clicked(self):
        if self.turno == 1:
            self.tateti.btn3.setText("X")
            self.matriz[0][2] = "x" 
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn3.setText("O")
            self.matriz[0][2] = "o" 
            self.turno = 1
        self.tateti.btn3.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn4Clicked(self):
        if self.turno == 1:
            self.tateti.btn4.setText("X")
            self.matriz[1][0] = "x" 
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn4.setText("O")
            self.matriz[1][0] = "o" 
            self.turno = 1
        self.tateti.btn4.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn5Clicked(self):
        if self.turno == 1:
            self.tateti.btn5.setText("X")
            self.matriz[1][1] = "x" 
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn5.setText("O")
            self.matriz[1][1] = "o" 
            self.turno = 1
        self.tateti.btn5.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn6Clicked(self):
        if self.turno == 1:
            self.tateti.btn6.setText("X")
            self.matriz[1][2] = "x"
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn6.setText("O")
            self.matriz[1][2] = "o"
            self.turno = 1
        self.tateti.btn6.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn7Clicked(self):
        if self.turno == 1:
            self.tateti.btn7.setText("X")
            self.matriz[2][0] = "x"
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn7.setText("O")
            self.matriz[2][0] = "o"
            self.turno = 1
        self.tateti.btn7.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn8Clicked(self):
        if self.turno == 1:
            self.tateti.btn8.setText("X")
            self.matriz[2][1] = "x"
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn8.setText("O")
            self.matriz[2][1] = "o"
            self.turno = 1
        self.tateti.btn8.setEnabled(False)
        self.contador += 1
        self.validarGanador()

    def btn9Clicked(self):
        if self.turno == 1:
            self.tateti.btn9.setText("X")
            self.matriz[2][2] = "x"
            self.turno = 2
        elif self.turno == 2:
            self.tateti.btn9.setText("O")
            self.matriz[2][2] = "o"
            self.turno = 1
        self.tateti.btn9.setEnabled(False)
        self.contador += 1
        self.validarGanador()

# -- Inicio de la app --

app = QtWidgets.QApplication([])
application = Tateti()
application.show()
sys.exit(app.exec())
