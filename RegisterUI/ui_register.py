# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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

import source5

class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(410, 630)
        Register.setStyleSheet(u"*{\n"
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
        self.centralwidget = QWidget(Register)
        self.centralwidget.setObjectName(u"centralwidget")
        self.contenedor = QFrame(self.centralwidget)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setGeometry(QRect(20, 10, 371, 611))
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.toolButton = QToolButton(self.contenedor)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(164, 20, 51, 51))
        icon = QIcon()
        icon.addFile(u":/images/images/icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(30, 30))
        self.registro = QLabel(self.contenedor)
        self.registro.setObjectName(u"registro")
        self.registro.setGeometry(QRect(30, 120, 111, 21))
        self.label = QLabel(self.contenedor)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 170, 151, 19))
        self.lineEdit = QLineEdit(self.contenedor)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 200, 321, 25))
        self.lineEdit.setMaxLength(16)
        self.label_2 = QLabel(self.contenedor)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 250, 151, 19))
        self.lineEdit_2 = QLineEdit(self.contenedor)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 280, 321, 25))
        self.lineEdit_2.setMaxLength(16)
        self.label_3 = QLabel(self.contenedor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 330, 151, 19))
        self.lineEdit_3 = QLineEdit(self.contenedor)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 360, 321, 25))
        self.lineEdit_3.setMaxLength(25)
        self.label_4 = QLabel(self.contenedor)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 410, 151, 19))
        self.lineEdit_4 = QLineEdit(self.contenedor)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 440, 321, 25))
        self.lineEdit_4.setMaxLength(12)
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.contenedor)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 530, 321, 34))        

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Register", None))
        self.toolButton.setText("")
        self.registro.setText(QCoreApplication.translate("Register", u"REGISTRO", None))
        self.label.setText(QCoreApplication.translate("Register", u"Nombre/s", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Nombre/s", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"Apellido/s", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Register", u"Apellido/s", None))
        self.label_3.setText(QCoreApplication.translate("Register", u"E-mail", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Register", u"example@mail.com", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"Contrase\u00f1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Register", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.pushButton.setText(QCoreApplication.translate("Register", u"CREAR CUENTA", None))
    # retranslateUi
