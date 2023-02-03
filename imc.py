# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'imc.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_IMC = QLabel(self.centralwidget)
        self.label_IMC.setObjectName(u"label_IMC")
        font = QFont()
        font.setPointSize(20)
        self.label_IMC.setFont(font)
        self.label_IMC.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_IMC)

        self.verticalSpacer = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_altura = QLabel(self.centralwidget)
        self.label_altura.setObjectName(u"label_altura")
        self.label_altura.setFont(font)
        self.label_altura.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_altura)

        self.lineEdit_altura = QLineEdit(self.centralwidget)
        self.lineEdit_altura.setObjectName(u"lineEdit_altura")

        self.verticalLayout.addWidget(self.lineEdit_altura)

        self.verticalSpacer_2 = QSpacerItem(20, 88, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.label_peso = QLabel(self.centralwidget)
        self.label_peso.setObjectName(u"label_peso")
        self.label_peso.setFont(font)
        self.label_peso.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_peso)

        self.lineEdit_peso = QLineEdit(self.centralwidget)
        self.lineEdit_peso.setObjectName(u"lineEdit_peso")

        self.verticalLayout.addWidget(self.lineEdit_peso)

        self.verticalSpacer_3 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.label_resultado = QLabel(self.centralwidget)
        self.label_resultado.setObjectName(u"label_resultado")
        self.label_resultado.setFont(font)
        self.label_resultado.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_resultado)

        self.lineEdit_resultado = QLineEdit(self.centralwidget)
        self.lineEdit_resultado.setObjectName(u"lineEdit_resultado")

        self.verticalLayout.addWidget(self.lineEdit_resultado)

        self.verticalSpacer_4 = QSpacerItem(20, 87, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.pushButton_calcular = QPushButton(self.centralwidget)
        self.pushButton_calcular.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setPointSize(15)
        self.pushButton_calcular.setFont(font1)

        self.verticalLayout.addWidget(self.pushButton_calcular)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)


        self.pushButton_calcular.clicked.connect(self.calc)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_IMC.setText(QCoreApplication.translate("MainWindow", u"IMC", None))
        self.label_altura.setText(QCoreApplication.translate("MainWindow", u"Altura", None))
        self.label_peso.setText(QCoreApplication.translate("MainWindow", u"Peso", None))
        self.label_resultado.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.pushButton_calcular.setText(QCoreApplication.translate("MainWindow", u"Calcular", None))
    # retranslateUi

    def calc(self):
            Altura=float(self.input_comp.text())
            Peso=float(self.input_largura.text())
            result=Peso/(Altura*Altura)
            self.result_calculo.setText(str(result))
        












if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())