import sys
from PyQt5 import QtGui
import PyQt5.QtWidgets as qw

class Mensaje(qw.QWidget):
    def __init__(self, parent=None):
        qw.QWidget.__init__(self, parent)

        self.setGeometry(700, 300, 640, 640)
        self.setWindowTitle("Basico 03")
        self.setWindowIcon(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png"))

        self.setToolTip("Esto es un <b><i>Widget</i></b> hecho con PyQt.") # Mensaje tooltip, puede usar RTF
        qw.QToolTip.setFont(QtGui.QFont("OldEnglish", 11)) # Fuente y tamaño de fuente

apli = qw.QApplication(sys.argv)
tip = Mensaje()
tip.show()

apli.exec_() # También se puede poner así.