import sys
from PyQt5 import QtGui
import PyQt5.QtWidgets as qw

class VentanaPrincipal(qw.QMainWindow):
    def __init__(self, ancho, alto):
        qw.QMainWindow.__init__(self)

        # Se crea la ventana:
        self.setGeometry(700, 300, ancho, alto)
        self.setWindowTitle("Basico 05 - Barra de menú")
        self.setWindowIcon(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png"))
        self.statusBar().showMessage("Cargado correctamente.")
        self.setToolTip("Esto es un <b><i>Widget</i></b> hecho con PyQt.")
        qw.QToolTip.setFont(QtGui.QFont("OldEnglish", 11))

        # Se crea el botón salir:
        btnSalir = qw.QPushButton("Cerrar", self)
        btnSalir.setGeometry(int((ancho-50)/2), int((alto-50)/2), 60, 45)
        btnSalir.setToolTip("Presionar para cerrar.")
        btnSalir.setShortcut("Ctrl+H")
        btnSalir.setStatusTip("Botón Cerrar")
        btnSalir.clicked.connect(qw.QApplication.instance().quit)

        # Se crea el elemento del menú llamado "salir":
        msalir = qw.QAction(QtGui.QIcon("Recursos/MCServer-icon-64x64.png"), "Salir", self)
        msalir.setShortcut("Shift+C")
        msalir.setStatusTip("Menú Salir")
        msalir.triggered.connect(qw.QApplication.instance().quit)
        #msalir.setToolTip("Acción Salir") # No aparece.

        #Se crea la barra de menú agregandolé el botón anteriormente creado:
        menu = self.menuBar()
        menu.setToolTip("Barra de menú")
        mArchivo = menu.addMenu("Archivo")
        mArchivo.addAction(msalir)
        #mArchivo.setStatusTip("Menú Archivo") # No aparece.

apli = qw.QApplication(sys.argv)
ventana = VentanaPrincipal(320, 280)
ventana.show()
sys.exit(apli.exec_())