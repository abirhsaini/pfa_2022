from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from abc0 import Ui_MainWindow
from interface import Ui_MainWindow1
import sys
##from abc1 import Ui_MainWindow2 as aaa


app=QApplication(sys.argv)
m=QtWidgets.QMainWindow()
widget=QtWidgets.QStackedWidget()
sc1=Ui_MainWindow()
sc1.setupUi(m)

##sc2=aa
##sc3=aaa
widget.addWidget(m)
##widget.addWidget(sc2)
##widget.addWidget(sc3)
widget.resize(1500,750)
widget.show()
sys.exit(app.exec_())





