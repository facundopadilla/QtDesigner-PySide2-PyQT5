# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(410, 630)
        Register.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget{\n"
"background-image: url(:/images/images/background_register.png);\n"
"}\n"
"\n"
"QFrame#contenedor{\n"
"background:#1d1d1d;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#2d89ef;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel#registro{\n"
"color:white;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QLabel{\n"
"font-weight:bold;\n"
"color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"border-bottom:1px solid white;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"background:#2d89ef;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#2b5797;\n"
"color:white;\n"
"border-radius:15px;\n"
"font-weight: bold;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(Register)
        self.centralwidget.setObjectName("centralwidget")
        self.contenedor = QtWidgets.QFrame(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(20, 10, 371, 611))
        self.contenedor.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QtWidgets.QFrame.Raised)
        self.contenedor.setObjectName("contenedor")
        self.toolButton = QtWidgets.QToolButton(self.contenedor)
        self.toolButton.setGeometry(QtCore.QRect(164, 20, 51, 51))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.registro = QtWidgets.QLabel(self.contenedor)
        self.registro.setGeometry(QtCore.QRect(30, 120, 111, 21))
        self.registro.setObjectName("registro")
        self.label = QtWidgets.QLabel(self.contenedor)
        self.label.setGeometry(QtCore.QRect(30, 170, 151, 19))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.contenedor)
        self.lineEdit.setGeometry(QtCore.QRect(30, 200, 321, 25))
        self.lineEdit.setMaxLength(16)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.contenedor)
        self.label_2.setGeometry(QtCore.QRect(30, 250, 151, 19))
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.contenedor)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 280, 321, 25))
        self.lineEdit_2.setMaxLength(16)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.contenedor)
        self.label_3.setGeometry(QtCore.QRect(30, 330, 151, 19))
        self.label_3.setObjectName("label_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.contenedor)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 360, 321, 25))
        self.lineEdit_3.setMaxLength(25)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_4 = QtWidgets.QLabel(self.contenedor)
        self.label_4.setGeometry(QtCore.QRect(30, 410, 151, 19))
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.contenedor)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 440, 321, 25))
        self.lineEdit_4.setMaxLength(12)
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(self.contenedor)
        self.pushButton.setGeometry(QtCore.QRect(30, 530, 321, 34))
        self.pushButton.setObjectName("pushButton")
        Register.setCentralWidget(self.centralwidget)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Register"))
        self.registro.setText(_translate("Register", "REGISTRO"))
        self.label.setText(_translate("Register", "Nombre/s"))
        self.lineEdit.setPlaceholderText(_translate("Register", "Nombre/s"))
        self.label_2.setText(_translate("Register", "Apellido/s"))
        self.lineEdit_2.setPlaceholderText(_translate("Register", "Apellido/s"))
        self.label_3.setText(_translate("Register", "E-mail"))
        self.lineEdit_3.setPlaceholderText(_translate("Register", "example@mail.com"))
        self.label_4.setText(_translate("Register", "Contraseña"))
        self.lineEdit_4.setPlaceholderText(_translate("Register", "•••••••••••"))
        self.pushButton.setText(_translate("Register", "CREAR CUENTA"))


import source5


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QMainWindow()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())
