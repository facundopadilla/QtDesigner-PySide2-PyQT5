# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tateti.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# @author: facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/
# WARNING! All changes made in this file will be lost!

# Diseñado por Facundo Padilla - https://www.github.com/facundopadilla
# Éste contenido es de uso libre y contiene licencia MIT, por lo tanto, no me responsabilizo de daños y prejuicios en el caso de su uso y/o modificación.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 319)
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background: #1d1d1d;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border: none;\n"
"color: white;\n"
"font-size: 24px;\n"
"}\n"
"\n"
"QPushButton#btnComenzar{\n"
"background: #2d89ef;\n"
"border-radius: 4px;\n"
"font-size: 15px;\n"
"}\n"
"\n"
"QPushButton#btnComenzar:hover{\n"
"background: #2b5797;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(20)
        sizePolicy.setVerticalStretch(20)
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setItalic(True)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 70, 20, 161))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(50, 110, 211, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(50, 170, 211, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(180, 70, 20, 161))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(200, 70, 51, 41))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setText("")
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(130, 70, 51, 41))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setText("")
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(60, 70, 51, 41))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setText("")
        self.btn1.setObjectName("btn1")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(60, 130, 51, 41))
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setText("")
        self.btn4.setObjectName("btn4")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(60, 190, 51, 41))
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn7.setText("")
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(130, 190, 51, 41))
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn8.setText("")
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(200, 190, 51, 41))
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn9.setText("")
        self.btn9.setObjectName("btn9")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(200, 130, 51, 41))
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn6.setText("")
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(130, 130, 51, 41))
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setText("")
        self.btn5.setObjectName("btn5")
        self.btnComenzar = QtWidgets.QPushButton(self.centralwidget)
        self.btnComenzar.setGeometry(QtCore.QRect(90, 260, 130, 34))
        self.btnComenzar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnComenzar.setObjectName("btnComenzar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TaTeTi - Facundo Padilla"))
        self.btnComenzar.setText(_translate("MainWindow", "Limpiar y jugar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
