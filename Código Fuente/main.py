import sys
from ventana8 import *
from coreAlgoritmo import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush,QStandardItemModel, QStandardItem,QColor
from PyQt5.QtWidgets import QMessageBox

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data
        self.colors = dict()
        self.hheaders = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  
        self.vheaders = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]
        if role == Qt.BackgroundRole:
                color = self.colors.get((index.row(), index.column()))
                if color is not None:
                    return color
        if role == QtCore.Qt.TextAlignmentRole:
            return QtCore.Qt.AlignCenter

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])
    
    def change_color(self, row, column, color):
        ix = self.index(row, column)
        self.colors[(row, column)] = color
        self.dataChanged.emit(ix, ix, (Qt.BackgroundRole,))
    
    def headerData(self, section, orientation, role):  
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.hheaders[section]
            if orientation == QtCore.Qt.Vertical:
                return self.vheaders[section]
        return QtCore.QVariant()

class interfazGUIa(QtWidgets.QWidget):
    laberinto=[]
    model2 = QStandardItemModel()
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.ui.botonGenerarLaberinto.clicked.connect(self.obtener)
        self.ui.actionPrimero_en_Amplitud.triggered.connect(self.primeroA)
        self.ui.actionPrimero_en_Profundidad.triggered.connect(self.primeroP) 
        self.ui.listaLaberinto.setModel(self.model2)
        
         
    def setColortoRow(table, rowIndex, color):
        for j in range(table.columnCount()):
            table.item(rowIndex, j).setBackground(color)

    def pintarCamino(self, listas):
        cell = '0'
        entrada = 'I'
        salida = 'F'
        for f in range (10):
            for c in range (10):
                if(self.laberinto[f][c]=="0"):
                    self.model.change_color(f,c,QBrush(Qt.white))
                elif (self.laberinto[f][c]=="x"):
                    self.model.change_color(f,c,QBrush(Qt.black))

        for f in listas[1]:
            if(f.val==cell or f.val==entrada or f.val==salida):
                self.model.change_color(f.nodoF,f.nodoC,QBrush(Qt.gray)) 
            else:
                self.model.change_color(f.nodoF,f.nodoC,QBrush(Qt.red)) 

        i=0
        f=0
        c=0
        listaCaminoSolucion=[]
        while i==0:
            for l in listas[1]:
                if (l.nodoF==f and l.nodoC==c):
                    listaCaminoSolucion.append(l)
                    if (l.nodoPadreF== "null" ):
                        i=1
                    else:
                        f=l.nodoPadreF
                        c=l.nodoPadreC

        for f in listas[0]:
             self.model.change_color(f.nodoF,f.nodoC,QBrush(QColor("orange")))

        for f in listaCaminoSolucion:
             self.model.change_color(f.nodoF,f.nodoC,QBrush(Qt.green))
        self.model.change_color(0,0,QBrush(Qt.cyan))
        self.model.change_color(9,9,QBrush(Qt.cyan))
        self.ui.tablaLaberinto.setVisible(True)
    
    def obtener(self):
        self.table = QtWidgets.QTableView()
        maze=[]
        maze=generarLaberinto()
        self.laberinto=maze
        data=[]
        for f in range (10):
            fila=[]
            for c in range (10):
                dato=maze[f][c]
                fila.append(str(dato))
            data.append(fila) 
        self.model = TableModel(data)
        self.ui.tablaLaberinto.setModel(self.model)
        for i in range(10):
           self.ui.tablaLaberinto.setColumnWidth(i,10)
        for f in range (10):
            for c in range (10):
                if(self.laberinto[f][c]=="0"):
                    self.model.change_color(f,c,QBrush(Qt.white))
                elif (self.laberinto[f][c]=="x"):
                    self.model.change_color(f,c,QBrush(Qt.black)) 
        self.model.change_color(0,0,QBrush(Qt.cyan))
        self.model.change_color(9,9,QBrush(Qt.cyan))
        self.ui.tablaLaberinto.setVisible(True) 
        self.model2.clear()
        self.ui.listaLaberinto.setModel(self.model2)
    
    def primeroA(self):
        if len(self.laberinto)>1:
            result=[]
            result.extend(algoritmosBusqueda(self.laberinto,0))
            self.pintarCamino(result)
            self.model2.clear()
            self.ui.listaLaberinto.setModel(self.model2)
            for i in result[2]:
                self.model2.appendRow(QStandardItem(i))
            self.ui.listaLaberinto.setModel(self.model2)
        else:
            QMessageBox.about(self, "Alerta", 'Debe generar un laberinto primero')
          
    def primeroP(self):
        if len(self.laberinto)>1:
            result=[]
            result.extend(algoritmosBusqueda(self.laberinto,1))
            self.pintarCamino(result)
            self.model2.clear()
            self.ui.listaLaberinto.setModel(self.model2)
            for i in result[2]:
                self.model2.appendRow(QStandardItem(i))
            self.ui.listaLaberinto.setModel(self.model2)
        else: 
            QMessageBox.about(self, "Alerta", 'Debe generar un laberinto primero')
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mi_app = interfazGUIa()
    mi_app.show()
    sys.exit(app.exec_())