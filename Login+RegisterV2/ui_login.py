# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from images import rcc_login


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(410, 630)
        Login.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget#loginwidget{\n"
"background:url(:/background/background.png)\n"
"}\n"
"\n"
"QFrame#framelogin{\n"
"background:#1d1d1d;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel#controlstocklabel{\n"
"font-size:24px;\n"
"}\n"
"\n"
"QToolButton#toolBtn{\n"
"background:#2d89ef;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"font-weight:bold;\n"
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
"border-radius:15px;\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background:#2b5797;\n"
"border-radius:15px;\n"
"color:white;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton#btnOlvidar{\n"
"background:transparent;\n"
"}\n"
"\n"
"QPushButton:hover#btnOlvidar{\n"
"border-bottom:1px solid white;\n"
"border-radius:0px;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.loginwidget = QtWidgets.QWidget(Login)
        self.loginwidget.setObjectName("loginwidget")
        self.framelogin = QtWidgets.QFrame(self.loginwidget)
        self.framelogin.setGeometry(QtCore.QRect(20, 9, 371, 611))
        self.framelogin.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelogin.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelogin.setObjectName("framelogin")
        self.controlstocklabel = QtWidgets.QLabel(self.framelogin)
        self.controlstocklabel.setGeometry(QtCore.QRect(120, 0, 151, 51))
        self.controlstocklabel.setObjectName("controlstocklabel")
        self.toolBtn = QtWidgets.QToolButton(self.framelogin)
        self.toolBtn.setGeometry(QtCore.QRect(170, 50, 51, 51))
        self.toolBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBtn.setIcon(icon)
        self.toolBtn.setIconSize(QtCore.QSize(30, 30))
        self.toolBtn.setObjectName("toolBtn")
        self.iniciarlabel = QtWidgets.QLabel(self.framelogin)
        self.iniciarlabel.setGeometry(QtCore.QRect(30, 150, 131, 19))
        self.iniciarlabel.setObjectName("iniciarlabel")
        self.entryUser = QtWidgets.QLineEdit(self.framelogin)
        self.entryUser.setGeometry(QtCore.QRect(30, 210, 321, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entryUser.sizePolicy().hasHeightForWidth())
        self.entryUser.setSizePolicy(sizePolicy)
        self.entryUser.setMaxLength(23)
        self.entryUser.setObjectName("entryUser")
        self.entryPass = QtWidgets.QLineEdit(self.framelogin)
        self.entryPass.setGeometry(QtCore.QRect(32, 290, 321, 25))
        self.entryPass.setMaxLength(12)
        self.entryPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.entryPass.setObjectName("entryPass")
        self.labelUser = QtWidgets.QLabel(self.framelogin)
        self.labelUser.setGeometry(QtCore.QRect(30, 180, 68, 19))
        self.labelUser.setObjectName("labelUser")
        self.labelPass = QtWidgets.QLabel(self.framelogin)
        self.labelPass.setGeometry(QtCore.QRect(30, 260, 101, 19))
        self.labelPass.setObjectName("labelPass")
        self.brnIniciar = QtWidgets.QPushButton(self.framelogin)
        self.brnIniciar.setGeometry(QtCore.QRect(30, 500, 321, 34))
        self.brnIniciar.setObjectName("brnIniciar")
        self.btnCrear = QtWidgets.QPushButton(self.framelogin)
        self.btnCrear.setGeometry(QtCore.QRect(30, 550, 321, 34))
        self.btnCrear.setObjectName("btnCrear")
        self.usericon = QtWidgets.QLabel(self.framelogin)
        self.usericon.setGeometry(QtCore.QRect(320, 210, 21, 21))
        self.usericon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.usericon.setText("")
        self.usericon.setTextFormat(QtCore.Qt.AutoText)
        self.usericon.setPixmap(QtGui.QPixmap(":/icon/user.png"))
        self.usericon.setScaledContents(True)
        self.usericon.setObjectName("usericon")
        self.passicon = QtWidgets.QLabel(self.framelogin)
        self.passicon.setGeometry(QtCore.QRect(320, 280, 21, 21))
        self.passicon.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passicon.setText("")
        self.passicon.setTextFormat(QtCore.Qt.AutoText)
        self.passicon.setPixmap(QtGui.QPixmap(":/icon/pass.png"))
        self.passicon.setScaledContents(True)
        self.passicon.setObjectName("passicon")
        self.btnOlvidar = QtWidgets.QPushButton(self.framelogin)
        self.btnOlvidar.setGeometry(QtCore.QRect(100, 330, 171, 34))
        self.btnOlvidar.setObjectName("btnOlvidar")
        Login.setCentralWidget(self.loginwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "ControlStock - Iniciar sesión"))
        self.controlstocklabel.setText(_translate("Login", "ControlStock"))
        self.iniciarlabel.setText(_translate("Login", "INICIAR SESIÓN"))
        self.entryUser.setPlaceholderText(_translate("Login", "Ingresar usuario"))
        self.entryPass.setPlaceholderText(_translate("Login", "•••••••••••"))
        self.labelUser.setText(_translate("Login", "Usuario"))
        self.labelPass.setText(_translate("Login", "Contraseña"))
        self.brnIniciar.setText(_translate("Login", "INICIAR SESIÓN"))
        self.btnCrear.setText(_translate("Login", "CREAR CUENTA"))
        self.btnOlvidar.setText(_translate("Login", "Olvidé mi contraseña"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
