import sys
from PySide2.QtWidgets import *
from ui_register import Ui_Register

class Register(QDialog):

    def __init__(self):
        super(Register, self).__init__() # inicializo la app
        self.register = Ui_Register() # obtengo la clase
        self.register.setupUi(self) # cargo las propiedades

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Register()
    myapp.show() # muestro la app
    sys.exit(app.exec_())
