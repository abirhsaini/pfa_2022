from PyQt5 import QtWidgets, QtCore, QtGui , uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QWidget()
MainWindow.setStyleSheet("background-color: #FFFFFF")

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("PFA")
        MainWindow.resize(1500,750)
        self.titre=QtWidgets.QLabel("Abbulkassis \n DR-AI",MainWindow)
        self.titre.setStyleSheet("color: #96C0B3 ; font-size: 25px ; font-family : Inter;")
        self.titre.resize(200,100)
        self.titre.move(350,0)
        self.titre1=QtWidgets.QLabel("    TELECHARGER",MainWindow)
        self.titre1.setStyleSheet('background-color: #000000; color: white ; font-size:20px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.titre1.resize(200,40)
        self.titre1.move(800,30)
        self.titre1.hide()
        ##self.btn=QtWidgets.QPushButton(MainWindow)
        ##self.btn.setIcon(QtGui.QIcon('PFA3.png'))
        self.photo=QtWidgets.QLabel(MainWindow)
        self.photo.move(230,-5)
        self.photo.resize(100,110)
        pic=QPixmap("PFA3.png").scaled(90,95)
        self.photo.setPixmap(pic)
        self.label=QtWidgets.QLabel("      Detection  ",MainWindow)
        self.label.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label.move(160,140)
        self.label.resize(120,40)
        self.label1=QtWidgets.QLabel("      Image FO  ",MainWindow)
        self.label1.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label1.move(600,140)
        self.label1.resize(120,40)
        self.label2=QtWidgets.QLabel("   Segmentation  ",MainWindow)
        self.label2.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label2.move(1040,140)
        self.label2.resize(120,40)
        self.photo1=QtWidgets.QLabel(MainWindow)
        self.photo1.move(65,200)
        self.photo1.resize(320,320)
        ##self.photo1.setStyleSheet(" border : 2px solid # ; border-radius: 18px ")
        pic1=QPixmap("PFA4.png").scaled(315,300)
        self.photo1.setStyleSheet(" border : 2px solid #000000 ; border-radius: 18px ")
        self.photo1.setPixmap(pic1)

        self.photo2=QtWidgets.QLabel(MainWindow)
        self.photo2.move(510,200)
        self.photo2.resize(320,320)
        ##self.photo1.setStyleSheet(" border : 2px solid # ; border-radius: 18px ")
        pic2=QPixmap("PFA4.png").scaled(315,300)
        self.photo2.setStyleSheet(" border : 2px solid #000000 ; border-radius: 18px ")
        self.photo2.setPixmap(pic2)

        self.photo3=QtWidgets.QLabel(MainWindow)
        self.photo3.move(940,200)
        self.photo3.resize(320,320)
        ##self.photo1.setStyleSheet(" border : 2px solid # ; border-radius: 18px ")
        pic3=QPixmap("PFA4.png").scaled(315,300)
        self.photo3.setStyleSheet(" border : 2px solid #000000 ; border-radius: 18px ")
        self.photo3.setPixmap(pic3)



        self.label3=QtWidgets.QLabel("  Nom du patient:    jk   ",MainWindow)
        self.label3.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label3.move(110,560)
        self.label3.resize(140,40)

        self.line=QtWidgets.QLineEdit(MainWindow)
        self.line.move(215,560)
        self.line.resize(420,40)
        self.line.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        

        
        self.label4=QtWidgets.QLabel("      DATE:  ",MainWindow)
        self.label4.setStyleSheet('background-color: #96C0B3; color: white ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label4.move(110,610)
        self.label4.resize(140,40)

        self.line1=QtWidgets.QLineEdit(MainWindow)
        self.line1.move(215,610)
        self.line1.resize(420,40)
        self.line1.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")

        self.line4=QtWidgets.QLineEdit(MainWindow)
        self.line4.move(820,550)
        self.line4.resize(440,100)
        self.line4.setStyleSheet("background-color: white ; font-size: 12px ; color: black; border : 2px solid #96C0B3 ; border-radius:18px")
        self.label4=QtWidgets.QLabel("  Commentaire:  ",MainWindow)
        self.label4.setStyleSheet(' color: #96C0B3 ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.label4.move(860,530)
        self.label4.resize(110,40)
        self.btn5 = QtWidgets.QPushButton("  Commentaire:  ", MainWindow)
        self.btn5.setStyleSheet( ' color: #96C0B3 ; font-size:12px ; border: 2px solid #96C0B3 ; border-radius:18px ; font family: Inter;')
        self.btn5.move(960, 590)
        self.btn5.resize(110, 40)






            
if __name__=="__main__":
    
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
        
