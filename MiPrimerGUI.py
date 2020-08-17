# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 17:54:27 2020

@author: Magh
"""

from sys import argv, exit
from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qw


class VentanaPrincipal(qw.QMainWindow):
    def __init__(self, vAncho, vAlto):
        qw.QMainWindow.__init__(self)
        
        #Defino la ventana:
        self.setGeometry(540, 300, vAncho, vAlto)
        self.setWindowTitle("Ventana de Pruebas")
        self.setWindowIcon(QtGui.QIcon('Recursos/MCServer-icon-64x64.png')) #Es posible usarlo desde VSCode
        #self.setWindowIcon(QtGui.QIcon('C:/Users/Moises/OneDrive - SENATI/GitHub/MiPrimerGUI/Recursos/Icon-Python_PyQt5.png'))
        #self.setWindowIcon(QtGui.QIcon("OneDrive - SENATI/GitHub/MiPrimerGUI/Recursos/MCServer-icon-64x64.png"))
        self.statusBar().showMessage("Reto listo")
        self.setToolTip("Esto es un <b><i>ToolTip</i></b> usando PyQt")
        qw.QToolTip.setFont(QtGui.QFont("Arial", 10))
        
        #Creo botón para salir:
        btnsalir = qw.QPushButton("Cerrar Aplicación", self)
        btnsalir.setToolTip("Botón que cierra la aplicación.")
        btnsalir.setGeometry((vAncho-100)/2, (vAlto-35)/2, 100, 35)
        #btnsalir.setShortcut("Ctrl+W") #No es necesario ya que se específica en el menú.
        btnsalir.setStatusTip("Cerrar aplicación.")
        btnsalir.clicked.connect(qw.QApplication.instance().quit)

        #Creo elemento del menú salir:
        menuSalir = qw.QAction(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png"), "Cerrar", self)
        menuSalir.setShortcut("Ctrl+Q")
        menuSalir.setStatusTip("Opción para Cerrar el aplicativo.")
        menuSalir.triggered.connect(qw.QApplication.instance().quit)

        #Creo la barra de menú, el menú archivo y le agrego el elemento salir:
        barraMenu = self.menuBar()
        barraMenu.setToolTip("Barra de Opciónes")
        menuArchivo = barraMenu.addMenu("&Archivo") #Funciona con y sin '&', por lo que su función aún no está clara.
        menuArchivo.addAction(menuSalir)


def main():
    app = qw.QApplication(argv)
    vPrincipal=VentanaPrincipal(800, 600)
    vPrincipal.show()
    exit(app.exec_())


if __name__ == "__main__":
    main()