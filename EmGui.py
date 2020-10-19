"""
Creado el día Jueves, Agosto 20 a las 16:46:07 del 2020

@author: Magh
"""

from PyQt5 import QtGui, QtCore
import PyQt5.QtWidgets as qw

class VentanaPrincipal(qw.QMainWindow):
    def __init__(self, vAncho, vAlto):
        qw.QMainWindow.__init__(self)
        
        #Defino la ventana:
        ventanaDim=[vAncho, vAlto]
        self.setGeometry(540, 300, ventanaDim[0], ventanaDim[1])
        self.setWindowTitle("Ventana de Pruebas")
        self.setWindowIcon(QtGui.QIcon('Recursos/MCServer-icon-64x64.png')) #Es posible usarlo desde VSCode
        #self.setWindowIcon(QtGui.QIcon('C:/Users/Moises/OneDrive - SENATI/GitHub/MiPrimerGUI/Recursos/Icon-Python_PyQt5.png'))
        #self.statusBar().showMessage("Ventana lista")
        self.setToolTip("Esto es un <b><i>ToolTip</i></b> usando PyQt")
        qw.QToolTip.setFont(QtGui.QFont("Arial", 10))

        #Creo la barra de menú y el menú archivo:
        barraMenu = self.menuBar()
        barraMenu.setToolTip("Barra de Opciónes")
        menuArchivo = barraMenu.addMenu("&Archivo") #Funciona con y sin '&', por lo que su función aún no está clara.

        #Creo elemento del menú 'salir':
        menuSalir = qw.QAction(QtGui.QIcon("Recursos/Icon-Python_PyQt5.png"), "Cerrar", self)
        menuSalir.setShortcut("Ctrl+Q")
        menuSalir.setStatusTip("Opción para cerrar el aplicativo.")
        menuSalir.triggered.connect(qw.QApplication.instance().quit)
        #Agrego el elemento a la barra de menú:
        menuArchivo.addAction(menuSalir) #Meterlo en una función y acceder por elemento. *miVar es una tupla.

        #Creo botón para salir:
        bSalirD=[100, 30]
        btnsalir = qw.QPushButton("Cerrar Aplicación", self)
        btnsalir.setToolTip("Botón que cierra la aplicación.")
        btnsalir.setGeometry(self.alinear(bSalirD, ventanaDim, "izqInf")[0], self.alinear(bSalirD, ventanaDim, "izqInf")[1], bSalirD[0], bSalirD[1])
        #btnsalir.setShortcut("Ctrl+W") #No es necesario ya que se específica en el menú.
        btnsalir.setStatusTip("Cerrar aplicación.")
        btnsalir.clicked.connect(qw.QApplication.instance().quit)

    #Crea la barra de menú con los elementos específicados:
    #def crearBarraMenu(self, *elementos): #Primero se indica el número de elementos
        #Creo la barra de menú y el menú archivo:
    #    barraMenu = self.menuBar()
    #    barraMenu.setToolTip("Barra de Opciones")
        #'&Archivo' Funciona con y sin '&', por lo que su función aún no está clara.
    #    menuArchivo = barraMenu.addMenu()
    #    menuArchivo.addAction(menuSalir)

    #Alinear al elemento deseado dentro de otro en base a las dimensiones de ambos elementos, si es una ventana 'menu' se queda en 'True':
    def alinear(self, objDim, vDim, lugar, barMenu=True, barEstado=True): #'Lugar' es solo una referencia en forma de cadena en dónde se quiere ubicar al objeto.
        alineado=[None, None]
        if barMenu: #Por defecto, 'menu' activado.
            alineado[1]=20
            vDim[1]-=20
        if barEstado:
            pass
        if lugar=='izqSup': #Alineamiento a la izquierda Superior.
            alineado[0]=0
            alineado[1]+=0
        elif lugar=='cenSup': #Alineamiento al centro Superior.
            alineado[0]=(vDim[0]/2)-(objDim[0]/2)
            alineado[1]+=0
        elif lugar=='derSup': #Alineamiento a la derecha Superior.
            alineado[0]=vDim[0]-objDim[0]
            alineado[1]+=0
        elif lugar=='izqCen' or lugar=='izquierda': #Alineamiento a la izquierda Centro o izquierda Global.
            alineado[0]=0
            alineado[1]+=(vDim[1]/2)-(objDim[1]/2)
        elif lugar=='centro': #Alineamiento al centro global.
            alineado[0]=(vDim[0]/2)-(objDim[0]/2)
            alineado[1]+=(vDim[1]/2)-(objDim[1]/2)
        elif lugar=='derCen' or lugar=='derecha': #Alineamiento a la derecha Centro o derecha Global.
            alineado[0]=vDim[0]-objDim[0]
            alineado[1]+=(vDim[1]/2)-(objDim[1]/2)
        elif lugar=='izqInf': #Alineamiento a la izquierda Inferior.
            alineado[0]=0
            alineado[1]+=vDim[1]-(objDim[1]/2)
        elif lugar=='cenInf': #Alineamiento al centro Inferior.
            alineado[0]=(vDim[0]/2)-(objDim[0]/2)
            alineado[1]+=vDim[1]-(objDim[1]/2)-10
        elif lugar=='derInf': #Alineamiento a la derecha Inferior.
            alineado[0]=vDim[0]-objDim[0]
            alineado[1]+=vDim[1]-(objDim[1]/2)-10
        else:
            print("<func: alinear>Error! No se reconoce el parámetro.")
        
        return alineado