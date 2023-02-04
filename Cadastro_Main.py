from Cadastro_p1 import *
import sys
import mysql.connector

con=mysql.connector.connect(host='localhost',database='cadPyside',user='root',password='suporte@10')
cur= con.cursor()

if con.is_connected():
    db_info = con.get_server_info()
    print("Banco de Dados Conectado Com Sucesso",db_info)


class Ui_MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema")

        self.pushButton_Confirmar.clicked.connect(self.cadastro)

    def cadastro(self):
        nome=self.lineEdit_Nome.text()
        email=self.lineEdit_Email.text()
        usuario=self.lineEdit_Usuario.text()
        senha=self.lineEdit_Senha.text()


        insert = f"INSERT INTO USUARIO (NOME,EMAIL,USUARIO,SENHA)VALUES ('{nome}','{email}','{usuario}','{senha}');"
        cur.execute(insert)
        con.commit()
        print(f"Usuario {nome}cadastrado com sucesso")
        
        msg=QMessageBox(self)
        msg.setWindowTitle("Cadastrado")
        msg.setText("Usuario cadastrado com sucesso")
        msg.exec()

        self.lineEdit_Nome.setText("")
        self.lineEdit_Email.setText("")
        self.lineEdit_Usuario.setText("")
        self.lineEdit_Senha.setText("")
        


if __name__ == "__main__":
    app=QApplication()
    janela=Ui_MainWindow()
    janela.show()
    app.exec()