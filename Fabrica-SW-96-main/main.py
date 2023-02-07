from Tela_Abrec_Main import *

class Ui_MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setupUi(self)


        self.btn_finalizar_as.clicked.connect(self.cadastro)

    def cadastro (self):
        self.lineEdit_nome_cuidador_as.text()
        self.lineEdit_cpf_cuidador_as.text()
        self.lineEdit_rg_cuidador_as.text()
        self.lineEdit_data_emissao_cuidador_as.text()
        self.lineEdit_orgao_expedidor_cuidador_as.text()
        self.lineEdit_telefone_cuidador_as.text()
        self.lineEdit_endereco_cuidador_as.text()
        self.lineEdit_cep_cuidador_as.text()
        self.lineEdit_bairro_cuidador_as.text()
        self.lineEdit_cidade_cuidador_as.text()
        self.lineEdit_parentesco_cuidador_as.text()


if __name__ == "__main__":
    app=QApplication()
    janela=Ui_MainWindow()
    janela.show()
    app.exec()