#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @author: Facundo Padilla - https://www.github.com/facundopadilla
# @linkedin: https://www.linkedin.com/in/facundopadilla/
# License MIT

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from ui_editor import Ui_MainWindow
import sys

class Editor(QtWidgets.QMainWindow):

    def __init__(self):
        super(Editor, self).__init__()

        self.editor = Ui_MainWindow()

        self.editor.setupUi(self)

        # -- Variables --

        self.contenido = ""
        self.ruta_del_archivo = ""

        # -- Variables de CONTROL --
        self.CONTROL_ruta_del_archivo = ""
        self.CONTROL_contenido = ""
        self.CONTROL_alerta1 = False
        self.CONTROL_alerta2 = False

        # -- Funciones menuBar --
        self.editor.actionNuevo.triggered.connect(self.nuevo_archivo) # cuando hagas click en 'Nuevo' en "Abrir -> Nuevo"
        self.editor.actionAbrir.triggered.connect(self.abrir_archivo) # cuando hagas click en 'Abrir' en "Abrir -> Abrir"
        self.editor.actionGuardar.triggered.connect(self.guardar_archivo) # cuando hagas click en 'Guardar' en "Abrir -> Guardar"
        self.editor.actionGuardar_como.triggered.connect(self.guardar_como) # cuando hagas click en 'Guardar como' en "Abrir -> Guardar como"

        # -- Ventana de alerta ---

        self.alerta = QMessageBox() # creo una caja de mensaje (QMessageBox), (def msgAlerta)

    # -- Def eventos --

    def nuevo_archivo(self):
        self.CONTROL_contenido = self.editor.textEdit.toPlainText() # obtener el contenido del textEdit
        if (self.contenido == self.CONTROL_contenido) and (self.ruta_del_archivo == self.CONTROL_ruta_del_archivo or self.ruta_del_archivo == ""):
            self.editor.textEdit.setText("") # limpio el contenido (textEdit)
            self.contenido = "" # libero memoria
            self.CONTROL_contenido = "" # libero memoria del control de contenido
        elif self.contenido != "" or self.contenido != self.CONTROL_contenido:
            self.msgAlerta(1) # alerta del tipo 1
            
    def abrir_archivo(self):
        self.CONTROL_contenido = self.editor.textEdit.toPlainText() # obtener el contenido del textEdit
        if (self.contenido == self.CONTROL_contenido) or (self.CONTROL_alerta2 == True):
            self.ruta_del_archivo = QFileDialog.getOpenFileName(None, "Selecciona un archivo", "", "Python (*.py);;Texto (*.txt)") # busco la dirección de donde está el archivo y filtro los archivos
            try: 
                self.archivo = open(f"{self.ruta_del_archivo[0]}", "r", encoding="utf-8") # como me retorna una lista, obtengo el path (ruta) y le digo que solo lo lea, y lo obtengo en utf-8
                self.contenido = ("").join(self.archivo.readlines()) # guardo el contenido
                self.archivo.close() # cierro el archivo para liberar memoria
                self.editor.textEdit.setText(self.contenido) # muestro el contenido en el textEdit
                self.CONTROL_contenido = self.contenido # hago el control de contenido
                self.setWindowTitle(f"Editor de texto - {self.ruta_del_archivo[0]}") # le modifico el título de la ventana
            except FileNotFoundError:
                pass # porque si no seleccionaste nada, no tiene que pasar nada
        elif self.CONTROL_alerta3 == False:
            self.msgAlerta(2) # alerta del tipo 2

    def guardar_archivo(self):
        self.CONTROL_contenido = self.editor.textEdit.toPlainText() # obtener el contenido del textEdit
        if self.ruta_del_archivo == self.CONTROL_ruta_del_archivo:
            self.ruta_del_archivo = QFileDialog.getSaveFileName(None, "Guardar archivo", "", "Python (*.py);;Texto (*.txt)") # filtro de como guardar el archivo
            try:
                self.archivo = open(self.ruta_del_archivo[0], "w", encoding="utf-8") # creo el archivo
                self.archivo.write(self.CONTROL_contenido) # añado contenido al archivo creado
                self.archivo.close() # cierro el archivo para liberar memoria
                self.setWindowTitle(f"Editor de texto - {self.ruta_del_archivo[0]}") # le modifico el título de la ventana
                self.CONTROL_ruta_del_archivo = self.ruta_del_archivo # control de ruta del archivo
            except FileNotFoundError:
                pass # si no guardo ningun archivo, no tiene que pasar nada
        elif self.ruta_del_archivo != "" and self.ruta_del_archivo == self.CONTROL_ruta_del_archivo:
            try:
                self.archivo = open(self.ruta_del_archivo[0], "w", encoding="utf-8") # creo el archivo
                self.archivo.write(self.contenido) # añado contenido al archivo creado
                self.archivo.close() # cierro el archivo para liberar memoria
            except FileNotFoundError:
                pass # si no guardo ningun archivo, no tiene que pasar nada
    
    def guardar_como(self):
        self.ruta_del_archivo = QFileDialog.getSaveFileName(None, "Guardar archivo") # no le paso ningun filtro, lo puede guardar en cualquier extensión
        try:
            self.archivo = open(self.ruta_del_archivo[0], "w", encoding="utf-8") # creo el archivo
            self.archivo.write(self.CONTROL_contenido) # añado contenido al archivo creado
            self.archivo.close() # cierro el archivo para liberar memoria
            self.setWindowTitle(f"Editor de texto - {self.ruta_del_archivo[0]}") # le modifico el título de la ventana
            self.CONTROL_ruta_del_archivo = self.ruta_del_archivo # creo el control de la ruta
        except FileNotFoundError:
            pass # si no guardo ningun archivo, no tiene que pasar nada

    # -- Mensajes de Alerta ---

    def msgAlerta(self, numero_error):
        if numero_error == 1:
            self.alerta.setWindowTitle("Alerta") # le defino un título
            self.alerta.setIcon(QMessageBox.Warning)
            self.alerta.setText(f"¿Estás seguro que quieres crear un nuevo archivo sin guardar?. No podrás recuperar lo que haz escrito.")
            self.alerta.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # botón de YES y botón de NO
            btnSi = self.alerta.button(QMessageBox.Yes) # Obtengo el botón YES
            btnSi.setText("Si") # le modifico el YES por el Si
            mostrar_alerta = self.alerta.exec_() # la ejecuto y muestro en pantalla
            if mostrar_alerta == QMessageBox.Yes:
                self.editor.textEdit.setText("") # le borro todo el contenido, si elige que NO, no pasa nada (no borra el texto)
        elif numero_error == 2:
            self.alerta.setWindowTitle("Alerta") # le defino un título
            self.alerta.setIcon(QMessageBox.Warning) # le indico un icono de "Warning" (peligro)
            self.alerta.setText(f"¿Estás seguro que quieres abrir un nuevo archivo sin guardar?. No podrás recuperar lo que haz escrito.")
            self.alerta.setStandardButtons(QMessageBox.Yes | QMessageBox.No) # botón de YES y botón de NO
            btnSi = self.alerta.button(QMessageBox.Yes) # Obtengo el botón YES
            btnSi.setText("Si") # le modifico el YES por el Si
            mostrar_alerta = self.alerta.exec_() # la ejecuto y muestro en pantalla
            if mostrar_alerta == QMessageBox.Yes:
                self.CONTROL_alerta2 = True
                self.abrir_archivo() # va a abrir otro archivo


# -- Iniciar la app --

app = QtWidgets.QApplication([])
application = Editor()
application.show()
sys.exit(app.exec())
