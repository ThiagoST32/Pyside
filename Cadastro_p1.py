# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerErDQPZ.ui'
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
        self.lineEdit_Nome = QLineEdit(self.centralwidget)
        self.lineEdit_Nome.setObjectName(u"lineEdit_Nome")
        self.lineEdit_Nome.setGeometry(QRect(90, 110, 113, 22))
        self.lineEdit_Email = QLineEdit(self.centralwidget)
        self.lineEdit_Email.setObjectName(u"lineEdit_Email")
        self.lineEdit_Email.setGeometry(QRect(90, 170, 113, 22))
        self.lineEdit_Usuario = QLineEdit(self.centralwidget)
        self.lineEdit_Usuario.setObjectName(u"lineEdit_Usuario")
        self.lineEdit_Usuario.setGeometry(QRect(90, 230, 113, 22))
        self.lineEdit_Senha = QLineEdit(self.centralwidget)
        self.lineEdit_Senha.setObjectName(u"lineEdit_Senha")
        self.lineEdit_Senha.setGeometry(QRect(90, 290, 113, 22))
        self.label_Senha = QLabel(self.centralwidget)
        self.label_Senha.setObjectName(u"label_Senha")
        self.label_Senha.setGeometry(QRect(40, 290, 49, 16))
        self.label_Usuario = QLabel(self.centralwidget)
        self.label_Usuario.setObjectName(u"label_Usuario")
        self.label_Usuario.setGeometry(QRect(40, 230, 49, 16))
        self.label_Email = QLabel(self.centralwidget)
        self.label_Email.setObjectName(u"label_Email")
        self.label_Email.setGeometry(QRect(40, 170, 49, 16))
        self.label_Nome = QLabel(self.centralwidget)
        self.label_Nome.setObjectName(u"label_Nome")
        self.label_Nome.setGeometry(QRect(40, 110, 49, 16))
        self.label_Cadastro = QLabel(self.centralwidget)
        self.label_Cadastro.setObjectName(u"label_Cadastro")
        self.label_Cadastro.setGeometry(QRect(40, 40, 111, 51))
        font = QFont()
        font.setPointSize(20)
        self.label_Cadastro.setFont(font)
        self.pushButton_Confirmar = QPushButton(self.centralwidget)
        self.pushButton_Confirmar.setObjectName(u"pushButton_Confirmar")
        self.pushButton_Confirmar.setGeometry(QRect(160, 350, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_Senha.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_Usuario.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.label_Email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_Nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_Cadastro.setText(QCoreApplication.translate("MainWindow", u"Cadastro", None))
        self.pushButton_Confirmar.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None))
    # retranslateUi




if __name__ == "__main__":

    app = QApplication(sys.argv)
    MainWindow =QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())