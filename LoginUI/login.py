import sys
from PySide2.QtWidgets import *
from ui.ui_login import Ui_Login

class Login(QDialog):

    def __init__(self):
        super(Login, self).__init__() # inicializo la app
        self.login = Ui_Login() # obtengo la clase
        self.login.setupUi(self) # cargo las propiedades

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = Login()
    myapp.show() # muestro la app
    sys.exit(app.exec_())
