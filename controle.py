from PyQt5 import uic, QtWidgets
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def funcao_principal():
    linha1 = sistema_cadastro.lineEdit.text()
    linha2 = sistema_cadastro.lineEdit_2.text()
    linha3 = sistema_cadastro.lineEdit_3.text()
    linha4 = sistema_cadastro.lineEdit_4.text()
    linha5 = sistema_cadastro.lineEdit_5.text()
    linha6 = sistema_cadastro.lineEdit_6.text()
    linha7 = sistema_cadastro.lineEdit_7.text()
    linha8 = sistema_cadastro.lineEdit_8.text()
    linha9 = sistema_cadastro.lineEdit_9.text()
    linha10 = sistema_cadastro.lineEdit_10.text()

    if sistema_cadastro.radioButton.isChecked():
        logging.info("Categoria Casa e Jardim foi selecionada")
    elif sistema_cadastro.radioButton_2.isChecked():
        logging.info("Categoria Ferramentas foi selecionada")
    elif sistema_cadastro.radioButton_3.isChecked():
        logging.info("Categoria Eletronicos foi selecionada")
    elif sistema_cadastro.radioButton_4.isChecked():
        logging.info("Categoria Smartphones foi selecionada")
    elif sistema_cadastro.radioButton_5.isChecked():
        logging.info("Categoria Tablets foi selecionada")
    elif sistema_cadastro.radioButton_6.isChecked():
        logging.info("Categoria Automotivo foi selecionada")
    elif sistema_cadastro.radioButton_7.isChecked():
        logging.info("Categoria Informatica foi selecionada")
    else:
        logging.info("Nenhuma categoria foi selecionada")

app = QtWidgets.QApplication([])
sistema_cadastro = uic.loadUi("sistema_cadastro.ui")
sistema_cadastro.pushButton.clicked.connect(funcao_principal)
sistema_cadastro.show()
app.exec()
