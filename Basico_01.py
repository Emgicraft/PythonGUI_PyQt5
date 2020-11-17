import sys
import PyQt5.QtWidgets as qw

apli = qw.QApplication(sys.argv)

widget = qw.QWidget()
widget.resize(640, 480)
widget.setWindowTitle("Basico 01")
widget.show()

sys.exit(apli.exec_())