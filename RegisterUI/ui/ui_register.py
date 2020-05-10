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


class Ui_Register(object):
    def setupUi(self, Register):
        if not Register.objectName():
            Register.setObjectName(u"Register")
        Register.resize(420, 630)
        Register.setStyleSheet(u"*{\n"
"font-family:century gothic;\n"
"background: url(C:/Users/Pc/Pictures/background_register.png);\n"
"}\n"
"\n"
"QToolButton{\n"
"background:#2d89ef;\n"
"border-radius:15px;\n"
"box-shadow: 2px 2px 10px #999;\n"
"}\n"
"\n"
"QLabel#label{\n"
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
"}\n"
"\n"
"QPushButton:hover{\n"
"background: #2b5797;\n"
"font-weight: bold;\n"
"}")
        self.frame = QFrame(Register)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 10, 381, 611))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 170, 91, 19))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 120, 111, 19))
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 200, 321, 25))
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 250, 91, 19))
        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(30, 280, 321, 25))
        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(30, 360, 321, 25))
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 330, 91, 19))
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 410, 91, 19))
        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(30, 440, 321, 25))
        self.lineEdit_4.setEchoMode(QLineEdit.Password)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(31, 530, 321, 34))
        self.toolButton = QToolButton(self.frame)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setGeometry(QRect(170, 20, 51, 51))
        icon = QIcon()
        icon.addFile(u"C:/Users/Pc/Downloads/sitio-web.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QSize(30, 30))

        self.retranslateUi(Register)

        QMetaObject.connectSlotsByName(Register)
    # setupUi

    def retranslateUi(self, Register):
        Register.setWindowTitle(QCoreApplication.translate("Register", u"Register", None))
        self.label_2.setText(QCoreApplication.translate("Register", u"Nombre/s", None))
        self.label.setText(QCoreApplication.translate("Register", u"REGISTRO", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Register", u"Nombre/s", None))
        self.label_3.setText(QCoreApplication.translate("Register", u"Apellido/s", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Register", u"Apellido/s", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("Register", u"example@mail.com", None))
        self.label_4.setText(QCoreApplication.translate("Register", u"Email", None))
        self.label_5.setText(QCoreApplication.translate("Register", u"Contrase\u00f1a", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("Register", u"\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022", None))
        self.pushButton.setText(QCoreApplication.translate("Register", u"CREAR CUENTA", None))
        self.toolButton.setText("")
    # retranslateUi

