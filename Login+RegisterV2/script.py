from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5 import uic, QtWidgets
from images import rcc_login
from ui_register import Ui_Register
import sys, ui_login

class Login(QMainWindow):

	# Login
	def __init__(self):
		super(Login, self).__init__() # inicializo
		uic.loadUi("login.ui", self) # cargo mi template.ui

		# Clicked connect (click botones)
		self.brnIniciar.clicked.connect(self.fn_validar)
		self.btnCrear.clicked.connect(self.fn_abrir)

	# Register - Open the new window - Abrir la ventana de registro
	def fn_abrir(self):
		self.ventana = QtWidgets.QMainWindow()
		self.ui = Ui_Register()
		self.ui.setupUi(self.ventana)
		self.ventana.show()

	# Funciones del login
	def fn_validar(self):
		usuario = self.entryUser.text() # obtengo el texto de entryUser
		password = self.entryPass.text() # obtengo el texto de entryPass
		if usuario == "" and password == "" :
			# Labels
			self.labelUser.setStyleSheet("color:red;")
			self.labelPass.setStyleSheet("color:red;")

			# LineEdits
			self.entryUser.setStyleSheet("""QLineEdit#entryUser{
				border-bottom:1px solid #ee1111;
				color:#ee1111;
				font-weight:bold;
				}
				""")
			self.entryPass.setStyleSheet("""QLineEdit#entryPass{
				border-bottom:1px solid #ee1111;
				color:#ee1111;
				font-weight:bold;
				}
				""")
		elif usuario != "" and password == "":
			self.labelPass.setStyleSheet("color:red;")
			self.entryPass.setStyleSheet("""QLineEdit#entryPass{
				border-bottom:1px solid #ee1111;
				color:#ee1111;
				font-weight:bold;
				}
				""")
			self.labelUser.setStyleSheet("color:white;")
			self.entryUser.setStyleSheet("""QLineEdit#entryUser{
				border-bottom:1px solid white;
				color:white;
				}
				""")
		elif usuario == "" and password != "":
			self.labelUser.setStyleSheet("color:red;")
			self.entryUser.setStyleSheet("""QLineEdit#entryUser{
				border-bottom:1px solid #ee1111;
				color:#ee1111;
				font-weight:bold;
				}
				""")
			self.labelPass.setStyleSheet("color:white;")
			self.entryPass.setStyleSheet("""QLineEdit#entryPass{
				border-bottom:1px solid white;
				color:white;
				}
				""")
		else:
			self.labelUser.setStyleSheet("color:white;")
			self.labelPass.setStyleSheet("color:white;")
			self.entryUser.setStyleSheet("""QLineEdit#entryUser{
				border-bottom:1px solid white;
				color:white;
				}
				""")
			self.entryPass.setStyleSheet("""QLineEdit#entryPass{
				border-bottom:1px solid white;
				color:white;
				}
				""")
		


if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    window = Login() 
    window.show() 
    sys.exit(app.exec_()) 