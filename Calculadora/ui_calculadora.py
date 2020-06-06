# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# @author: facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/
#
# WARNING! All changes made in this file will be lost!

# PARTE VISUAL --- NO HAY QUE TOCAR NADA!!!
# THIS PART IS VISUAL --- DON'T EDIT ANYTHING!!!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(451, 314)
        MainWindow.setStyleSheet("*{\n"
"font-family: century gothic;\n"
"}\n"
"\n"
"QWidget#centralwidget{\n"
"background-color: #1d1d1d;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"border: 1px solid white;\n"
"border-radius: 4px;\n"
"background-color:#2d89ef;\n"
"}\n"
"\n"
"QPushButton{\n"
"border-radius: 4px;\n"
"background-color: #2d89ef;\n"
"color:white;\n"
"font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: #2b5797;\n"
"}\n"
"\n"
"QLabel#alumno{\n"
"background-color: none;\n"
"border:none;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.resultadoLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultadoLabel.setGeometry(QtCore.QRect(44, 30, 321, 51))
        self.resultadoLabel.setText("")
        self.resultadoLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.resultadoLabel.setObjectName("resultadoLabel")
        self.btn7 = QtWidgets.QPushButton(self.centralwidget)
        self.btn7.setGeometry(QtCore.QRect(100, 120, 47, 31))
        self.btn7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn7.setObjectName("btn7")
        self.btn8 = QtWidgets.QPushButton(self.centralwidget)
        self.btn8.setGeometry(QtCore.QRect(150, 120, 47, 31))
        self.btn8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn8.setObjectName("btn8")
        self.btn9 = QtWidgets.QPushButton(self.centralwidget)
        self.btn9.setGeometry(QtCore.QRect(200, 120, 47, 31))
        self.btn9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn9.setObjectName("btn9")
        self.btn6 = QtWidgets.QPushButton(self.centralwidget)
        self.btn6.setGeometry(QtCore.QRect(200, 160, 47, 31))
        self.btn6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn6.setObjectName("btn6")
        self.btn5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn5.setGeometry(QtCore.QRect(150, 160, 47, 31))
        self.btn5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn5.setObjectName("btn5")
        self.btn4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn4.setGeometry(QtCore.QRect(100, 160, 47, 31))
        self.btn4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn4.setObjectName("btn4")
        self.btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn3.setGeometry(QtCore.QRect(200, 200, 47, 31))
        self.btn3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn3.setObjectName("btn3")
        self.btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn2.setGeometry(QtCore.QRect(150, 200, 47, 31))
        self.btn2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn2.setObjectName("btn2")
        self.btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn1.setGeometry(QtCore.QRect(100, 200, 47, 31))
        self.btn1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn1.setObjectName("btn1")
        self.btnPunto = QtWidgets.QPushButton(self.centralwidget)
        self.btnPunto.setGeometry(QtCore.QRect(100, 240, 47, 31))
        self.btnPunto.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnPunto.setObjectName("btnPunto")
        self.btn0 = QtWidgets.QPushButton(self.centralwidget)
        self.btn0.setGeometry(QtCore.QRect(150, 240, 47, 31))
        self.btn0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn0.setObjectName("btn0")
        self.btnResultado = QtWidgets.QPushButton(self.centralwidget)
        self.btnResultado.setGeometry(QtCore.QRect(200, 240, 47, 31))
        self.btnResultado.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnResultado.setObjectName("btnResultado")
        self.btnMultiplicar = QtWidgets.QPushButton(self.centralwidget)
        self.btnMultiplicar.setGeometry(QtCore.QRect(260, 120, 71, 31))
        self.btnMultiplicar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnMultiplicar.setObjectName("btnMultiplicar")
        self.btnDividir = QtWidgets.QPushButton(self.centralwidget)
        self.btnDividir.setGeometry(QtCore.QRect(260, 160, 71, 31))
        self.btnDividir.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnDividir.setObjectName("btnDividir")
        self.btnSumar = QtWidgets.QPushButton(self.centralwidget)
        self.btnSumar.setGeometry(QtCore.QRect(260, 200, 71, 31))
        self.btnSumar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnSumar.setObjectName("btnSumar")
        self.btnRestar = QtWidgets.QPushButton(self.centralwidget)
        self.btnRestar.setGeometry(QtCore.QRect(260, 240, 71, 31))
        self.btnRestar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnRestar.setObjectName("btnRestar")
        self.btnC = QtWidgets.QPushButton(self.centralwidget)
        self.btnC.setGeometry(QtCore.QRect(370, 30, 31, 51))
        self.btnC.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnC.setObjectName("btnC")
        self.alumno = QtWidgets.QLabel(self.centralwidget)
        self.alumno.setGeometry(QtCore.QRect(60, 290, 322, 19))
        self.alumno.setObjectName("alumno")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculadora - FacundoKimbo"))
        self.btn7.setText(_translate("MainWindow", "7"))
        self.btn8.setText(_translate("MainWindow", "8"))
        self.btn9.setText(_translate("MainWindow", "9"))
        self.btn6.setText(_translate("MainWindow", "6"))
        self.btn5.setText(_translate("MainWindow", "5"))
        self.btn4.setText(_translate("MainWindow", "4"))
        self.btn3.setText(_translate("MainWindow", "3"))
        self.btn2.setText(_translate("MainWindow", "2"))
        self.btn1.setText(_translate("MainWindow", "1"))
        self.btnPunto.setText(_translate("MainWindow", "."))
        self.btn0.setText(_translate("MainWindow", "0"))
        self.btnResultado.setText(_translate("MainWindow", "="))
        self.btnMultiplicar.setText(_translate("MainWindow", "X"))
        self.btnDividir.setText(_translate("MainWindow", "/"))
        self.btnSumar.setText(_translate("MainWindow", "+"))
        self.btnRestar.setText(_translate("MainWindow", "-"))
        self.btnC.setText(_translate("MainWindow", "C"))
        self.alumno.setText(_translate("MainWindow", "https://www.github.com/facundokimbo"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
