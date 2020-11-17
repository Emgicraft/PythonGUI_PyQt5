import sys
from PyQt5 import QtGui
import PyQt5.QtWidgets as qw

class Icono(qw.QWidget):
    def __init__(self, parent=None):
        qw.QWidget.__init__(self, parent)

        self.setGeometry(650, 360, 640, 320) # Ubicación: x, y & Tamaño: x, y
        self.setWindowTitle("Mi Icono")
        self.setWindowIcon(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png")) # Ruta del icono

apli = qw.QApplication(sys.argv)
icon = Icono()
icon.show()

sys.exit(apli.exec_())