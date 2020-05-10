# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login rojo.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.setWindowModality(Qt.NonModal)
        Login.setEnabled(True)
        Login.resize(480, 640)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(480, 640))
        Login.setMaximumSize(QSize(480, 640))
        Login.setStyleSheet(u"*{\n"
"font-family:century gothic;\n"
"font-size:24px;\n"
"background:url(C:/Users/Pc/Downloads/background4.jpg);\n"
"}\n"
"\n"
"QFrame{\n"
"background:rgba(0,0,0,0.8);\n"
"border-radius:15px;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"background:red;\n"
"border-radius: 50px;\n"
"}\n"
"\n"
"QToolButton{\n"
"background:red;\n"
"border-radius: 30px;\n"
"}\n"
"\n"
"QToolButton#tbtn2{\n"
"background:transparent;\n"
"border:white;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"background:transparent;\n"
"}\n"
"\n"
"QLabel#labelError{\n"
"color:red;\n"
"}\n"
"\n"
"QPushButton#btnEntrar{\n"
"background:red;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QPushButton#btnEntrar:hover{\n"
"background:#8B0000;\n"
"color:white;\n"
"border-radius:15px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background:transparent;\n"
"border:none;\n"
"color:#717072;\n"
"border-bottom:1px solid #717072;\n"
"}\n"
"")
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 90, 421, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_arriba = QLabel(self.frame)
        self.label_arriba.setObjectName(u"label_arriba")
        self.label_arriba.setGeometry(QRect(140, 60, 151, 31))
        self.btnEntrar = QPushButton(self.frame)
        self.btnEntrar.setObjectName(u"btnEntrar")
        self.btnEntrar.setGeometry(QRect(100, 420, 231, 34))
        self.lineUser = QLineEdit(self.frame)
        self.lineUser.setObjectName(u"lineUser")
        self.lineUser.setGeometry(QRect(100, 160, 231, 31))
        self.lineUser.setMaxLength(12)
        self.lineUser.setAlignment(Qt.AlignCenter)
        self.linePass = QLineEdit(self.frame)
        self.linePass.setObjectName(u"linePass")
        self.linePass.setGeometry(QRect(100, 250, 231, 31))
        self.linePass.setMaxLength(12)
        self.linePass.setEchoMode(QLineEdit.Password)
        self.linePass.setAlignment(Qt.AlignCenter)
        self.tbtnArriba = QToolButton(Login)
        self.tbtnArriba.setObjectName(u"tbtnArriba")
        self.tbtnArriba.setGeometry(QRect(210, 50, 71, 71))
        icon = QIcon()
        icon.addFile(u"C:/Users/Pc/Downloads/hombres.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tbtnArriba.setIcon(icon)
        self.tbtnArriba.setIconSize(QSize(30, 30))

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label_arriba.setText(QCoreApplication.translate("Login", u"Iniciar sesi\u00f3n", None))
        self.btnEntrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.lineUser.setInputMask("")
        self.lineUser.setText("")
        self.lineUser.setPlaceholderText(QCoreApplication.translate("Login", u"Usuario", None))
        self.linePass.setInputMask("")
        self.linePass.setText("")
        self.linePass.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.tbtnArriba.setText("")
    # retranslateUi



