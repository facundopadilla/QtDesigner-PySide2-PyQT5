# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# @author: facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from images import rcc_register

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(420, 630)
        Register.setStyleSheet("*{\n"
"font-family:century gothic;\n"
"background:url(:/background/background.png)\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#2d89ef;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel#labelRegistro{\n"
"color:white;\n"
"background:transparent;\n"
"font-weight: bold;\n"
"font-size:24px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QFrame{\n"
"background:#1d1d1d;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QFrame#frame2{\n"
"background:#2d89ef;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:white;\n"
"border-bottom:1px solid white;\n"
"font-family:century gothic;\n"
"}\n"
"\n"
"QPushButton{\n"
"background: #2d89ef;\n"
"color:white;\n"
"border-radius:15px;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:  #2b5797;\n"
"}")
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setGeometry(QtCore.QRect(20, 10, 381, 611))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.labelNombre = QtWidgets.QLabel(self.frame)
        self.labelNombre.setGeometry(QtCore.QRect(30, 170, 91, 19))
        self.labelNombre.setObjectName("labelNombre")
        self.labelRegistro = QtWidgets.QLabel(self.frame)
        self.labelRegistro.setGeometry(QtCore.QRect(30, 120, 111, 19))
        self.labelRegistro.setObjectName("labelRegistro")
        self.entryNombre = QtWidgets.QLineEdit(self.frame)
        self.entryNombre.setGeometry(QtCore.QRect(30, 200, 321, 25))
        self.entryNombre.setObjectName("entryNombre")
        self.labelApellido = QtWidgets.QLabel(self.frame)
        self.labelApellido.setGeometry(QtCore.QRect(30, 250, 91, 19))
        self.labelApellido.setObjectName("labelApellido")
        self.entryApellido = QtWidgets.QLineEdit(self.frame)
        self.entryApellido.setGeometry(QtCore.QRect(30, 280, 321, 25))
        self.entryApellido.setObjectName("entryApellido")
        self.entryEmail = QtWidgets.QLineEdit(self.frame)
        self.entryEmail.setGeometry(QtCore.QRect(30, 360, 321, 25))
        self.entryEmail.setObjectName("entryEmail")
        self.labelEmail = QtWidgets.QLabel(self.frame)
        self.labelEmail.setGeometry(QtCore.QRect(30, 330, 91, 19))
        self.labelEmail.setObjectName("labelEmail")
        self.labelPass = QtWidgets.QLabel(self.frame)
        self.labelPass.setGeometry(QtCore.QRect(30, 410, 91, 19))
        self.labelPass.setObjectName("labelPass")
        self.entryPass = QtWidgets.QLineEdit(self.frame)
        self.entryPass.setGeometry(QtCore.QRect(30, 440, 321, 25))
        self.entryPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entryPass.setObjectName("entryPass")
        self.btnCrear = QtWidgets.QPushButton(self.frame)
        self.btnCrear.setGeometry(QtCore.QRect(31, 500, 321, 34))
        self.btnCrear.setObjectName("btnCrear")
        self.toolButton = QtWidgets.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(170, 20, 51, 51))
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.btnVolver = QtWidgets.QPushButton(self.frame)
        self.btnVolver.setGeometry(QtCore.QRect(30, 550, 321, 34))
        self.btnVolver.setObjectName("btnVolver")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Registro"))
        self.labelNombre.setText(_translate("Register", "Nombre/s"))
        self.labelRegistro.setText(_translate("Register", "REGISTRO"))
        self.entryNombre.setPlaceholderText(_translate("Register", "Nombre/s"))
        self.labelApellido.setText(_translate("Register", "Apellido/s"))
        self.entryApellido.setPlaceholderText(_translate("Register", "Apellido/s"))
        self.entryEmail.setPlaceholderText(_translate("Register", "example@mail.com"))
        self.labelEmail.setText(_translate("Register", "E-mail"))
        self.labelPass.setText(_translate("Register", "Contraseña"))
        self.entryPass.setPlaceholderText(_translate("Register", "•••••••••••"))
        self.btnCrear.setText(_translate("Register", "CREAR CUENTA"))
        self.btnVolver.setText(_translate("Register", "VOLVER"))
