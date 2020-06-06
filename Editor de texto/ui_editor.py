# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editor.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
# @author: facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/
#
# WARNING! All changes made in this file will be lost!

# PARTE VISUAL --- NO EDITAR NADA!!!
# THIS PART IS VISUAL --- DON'T EDIT ANYTHING!!!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(617, 578)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("*{\n"
"color:white;\n"
"}\n"
"\n"
"QTextEdit{\n"
"font-size: 18px;\n"
"background-color: #1d1d1d;\n"
"color: white;\n"
"font-family: arial;\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: #1d1d1d;\n"
"}\n"
"\n"
"QMenuBar:item{\n"
"background-color: #1d1d1d;\n"
"}\n"
"\n"
"QMenuBar:item:selected{\n"
"background-color: #292929;\n"
"}\n"
"\n"
"QMenu{\n"
"background-color: #1d1d1d;\n"
"}\n"
"\n"
"QMenu:item:selected{\n"
"background-color: #292929;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("arial")
        font.setPointSize(-1)
        self.textEdit.setFont(font)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textEdit.setFrameShape(QtWidgets.QFrame.Box)
        self.textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 31))
        self.menubar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menubar.setObjectName("menubar")
        self.menuAbrir = QtWidgets.QMenu(self.menubar)
        self.menuAbrir.setObjectName("menuAbrir")
        self.menuAutor = QtWidgets.QMenu(self.menubar)
        self.menuAutor.setObjectName("menuAutor")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNuevo = QtWidgets.QAction(MainWindow)
        self.actionNuevo.setObjectName("actionNuevo")
        self.actionGuardar = QtWidgets.QAction(MainWindow)
        self.actionGuardar.setObjectName("actionGuardar")
        self.actionGuardar_como = QtWidgets.QAction(MainWindow)
        self.actionGuardar_como.setObjectName("actionGuardar_como")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.menuAbrir.addAction(self.actionNuevo)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionAbrir)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionGuardar)
        self.menuAbrir.addSeparator()
        self.menuAbrir.addAction(self.actionGuardar_como)
        self.menuAbrir.addSeparator()
        self.menubar.addAction(self.menuAbrir.menuAction())
        self.menubar.addAction(self.menuAutor.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editor de texto"))
        self.menuAbrir.setTitle(_translate("MainWindow", "Archivo"))
        self.menuAutor.setTitle(_translate("MainWindow", "https://www.github.com/facundopadilla"))
        self.actionNuevo.setText(_translate("MainWindow", "Nuevo"))
        self.actionGuardar.setText(_translate("MainWindow", "Guardar"))
        self.actionGuardar_como.setText(_translate("MainWindow", "Guardar como"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
