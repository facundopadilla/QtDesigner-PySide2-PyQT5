from PyQt5 import QtWidgets
from ui_calculadora import Ui_MainWindow
import sys

class Calculadora(QtWidgets.QMainWindow): # creo una clase del tipo Calculadora donde recibe de QtWidgets la ventana QMainWindow (definido en el QtDesigner)

	def __init__(self): # mi constructor

		super(Calculadora, self).__init__() # heredo de QtWidgets.QMainWindow

		self.calculadora = Ui_MainWindow() # creo mi atributo calculadora que es igual a la clase Ui_MainWindow()

		self.calculadora.setupUi(self) # obtengo los atributos de Ui_MainWindow()

		self.resultado = "" # creo un atributo donde se guardará el resultado

		# --- Clicked Connect ---
		self.calculadora.btn0.clicked.connect(self.btn0Clicked) # cuando hago click en el boton 0
		self.calculadora.btn1.clicked.connect(self.btn1Clicked) # cuando hago click en el boton 1
		self.calculadora.btn2.clicked.connect(self.btn2Clicked) # cuando hago click en el boton 2
		self.calculadora.btn3.clicked.connect(self.btn3Clicked) # cuando hago click en el boton 3
		self.calculadora.btn4.clicked.connect(self.btn4Clicked) # cuando hago click en el boton 4
		self.calculadora.btn5.clicked.connect(self.btn5Clicked) # cuando hago click en el boton 5
		self.calculadora.btn6.clicked.connect(self.btn6Clicked) # cuando hago click en el boton 6
		self.calculadora.btn7.clicked.connect(self.btn7Clicked) # cuando hago click en el boton 7
		self.calculadora.btn8.clicked.connect(self.btn8Clicked) # cuando hago click en el boton 8
		self.calculadora.btn9.clicked.connect(self.btn9Clicked) # cuando hago click en el boton 9
		self.calculadora.btnC.clicked.connect(self.btnCClicked) # cuando hago click en el boton C
		self.calculadora.btnSumar.clicked.connect(self.btnSumarClicked) # cuando hago click en el boton +
		self.calculadora.btnRestar.clicked.connect(self.btnRestarClicked) # cuando hago click en el boton -
		self.calculadora.btnMultiplicar.clicked.connect(self.btnMultiplicarClicked) # cuando hago click en el boton *
		self.calculadora.btnDividir.clicked.connect(self.btnDividirClicked) # cuando hago click en el boton /
		self.calculadora.btnPunto.clicked.connect(self.btnPuntoClicked) #cuando hago click en el boton . (punto)
		self.calculadora.btnResultado.clicked.connect(self.obtenerResultado) # cuando hago click en el boton = (para obtener el resultado)

	# -- Funciones --
	def resultadoNuevo(self, resultado):
		try: 
			self.calculadora.resultadoLabel.setText(self.resultado) # me dá el resultado final
		except:
			self.calculadora.resultadoLabel.setText("Hubo un error, inténtalo nuevamente. ")

	# función cuando hago click en el botón C		
	def btnCClicked(self):
		self.resultado = self.resultado[:-1] # obtengo el resultado desde el comienzo pero evitando el valor final
		self.resultadoNuevo(self.resultado) # paso como parametro mi resultado y lo modifica la función resultadoNuevo()

	# función cuando hago click en el boton =
	def obtenerResultado(self, resultado):
		if self.resultado == "":
			self.calculadora.resultadoLabel.setText("No añadiste ningún número") # si hace click en el btnResultado y no haya ningún número
		elif self.resultado != "":
			try:
				self.resultado = str(eval(self.resultado)) # evalúa el resultado de self.resultado y se lo re asigno
				self.resultadoNuevo(self.resultado) # le envío el resultado nuevo
			except:
				self.calculadora.resultadoLabel.setText("Hubo un error, inténtalo nuevamente. ")

	# función cuando hago click en el botón 0
	def btn0Clicked(self):
		self.resultado += "0" # añado el 0
		self.resultadoNuevo(self.resultado) # modifico 
	
	# función cuando hago click en el botón 1
	def btn1Clicked(self):
		self.resultado += "1" # añado el 1
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón 2
	def btn2Clicked(self):
		self.resultado += "2" # añado el 2
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón 3
	def btn3Clicked(self):
		self.resultado += "3" # añado el 3
		self.resultadoNuevo(self.resultado) # modifico
	
	# función cuando hago click en el botón 4
	def btn4Clicked(self):
		self.resultado += "4" # añado el 4
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón 5
	def btn5Clicked(self):
		self.resultado += "5" # añado el 5
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón 6
	def btn6Clicked(self):
		self.resultado += "6" # añado el 6
		self.resultadoNuevo(self.resultado) # modifico
	
	# función cuando hago click en el botón 7
	def btn7Clicked(self):
		self.resultado += "7" # añado el 7
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón 8
	def btn8Clicked(self):
		self.resultado += "8" # añado el 8
		self.resultadoNuevo(self.resultado) # modifico
	
	# función cuando hago click en el botón 9
	def btn9Clicked(self):
		self.resultado += "9" # añado el 9
		self.resultadoNuevo(self.resultado) # modifico
 
	# función cuando hago click en el botón +
	def btnSumarClicked(self):
		self.resultado += "+" # añado el signo +
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón -
	def btnRestarClicked(self):
		self.resultado += "-" # añado el signo -
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón *
	def btnMultiplicarClicked(self):
		self.resultado += "*" # añado el signo *
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón /
	def btnDividirClicked(self):
		self.resultado += "/" # añado el signo /
		self.resultadoNuevo(self.resultado) # modifico

	# función cuando hago click en el botón . (punto)
	def btnPuntoClicked(self):
		self.resultado += "." # añado el punto
		self.resultadoNuevo(self.resultado) # 

	# --- OBTENER EVENTOS POR TECLADO ---
	def keyPressEvent(self, event):
		if event.key() == 16777219: # boton de retroceso/borrar
			self.resultado = self.resultado[:-1] # me borra el último elemento
		elif 16777220 <= event.key() <= 16777221: # botones de enter o intro
			self.obtenerResultado(self.resultado) # obtengo el resultado
		elif 42 <= event.key() <= 57: # los números incluido del punto, *, /, +, -
			self.resultado += str(event.text()) # event.text() transforma el event.key() al valor correspondiente
		self.resultadoNuevo(self.resultado) #  envío el nuevo resultado

# -- INICIALIZACIÓN DE LA APP --
app = QtWidgets.QApplication([]) # obtengo los widgets de mi aplicación

application = Calculadora() # creo un objeto del tipo Calculadora()

application.show() # muestro mi objeto del tipo Calculadora()

sys.exit(app.exec()) # muestro en pantalla