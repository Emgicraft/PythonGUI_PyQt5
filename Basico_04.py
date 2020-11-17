import sys
from PyQt5 import QtGui
import PyQt5.QtWidgets as qw

class BotonSalir(qw.QWidget):
    def __init__(self, parent=None):
        qw.QWidget.__init__(self, parent)

        self.setGeometry(700, 300, 320, 320)
        self.setWindowTitle("Basico 04 - Cerrar con un Botón")
        self.setWindowIcon(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png"))
        self.setToolTip("Esto es un <b><i>Widget</i></b> hecho con PyQt.")
        qw.QToolTip.setFont(QtGui.QFont("OldEnglish", 11))

        btnSalir = qw.QPushButton("Cerrar", parent=self)
        btnSalir.setGeometry(120, 150, 60, 35) # Ubicación: x, y & Tamaño: x, y
        # Cuando el botón sea clickeado, conectará con la instancia de salida:
        btnSalir.clicked.connect(qw.QApplication.instance().quit)

apli = qw.QApplication(sys.argv)
bs = BotonSalir()
bs.show()
sys.exit(apli.exec_())