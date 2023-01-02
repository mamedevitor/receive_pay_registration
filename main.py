from PySide6 import QtCore
from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget)
from matplotlib.pyplot import connect
from ui_main import Ui_MainWindow
from api_consultarcnpj import *
import sys
import pandas as pd
import datetime
from sql_query import data_base

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Sistema de Gerenciamento")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)


        #################################
        #TOGGLE BUTTON
        self.btn_toggle.clicked.connect(self.leftContainer)
        ###################################################

        #############################################################################################
        #Páginas do Sistema
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastrar))
        self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_pg_cadastro.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        
        #############################################################################################
        #Botões
        self.btn_cadastraremp.clicked.connect(self.new_record_comp)
        self.txt_cnpj.editingFinished.connect(self.consulta_api)
        ###########################################################
        self.buscar_dados()
        ############################################################
        
    def leftContainer(self):
        width = self.left_container.width()

        if width == 9:
            newWidth = 200
        else:
            newWidth = 9

        self.animation = QtCore.QPropertyAnimation(self.left_container, b"maximumWidth")
        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        
    def consulta_api(self):
        campos_cadastro = consultar_cnpj(self.txt_cnpj.text())
        
        self.txt_nomempresa.setText(campos_cadastro[2])
        self.txt_dtabertura.setText(campos_cadastro[1])
        self.txt_porte.setText(campos_cadastro[9])
        self.txt_situacao.setText(campos_cadastro[3])
        self.txt_logradouro.setText(campos_cadastro[4])
        self.txt_numeroemp.setText(campos_cadastro[5])
        self.txt_complemento.setText(campos_cadastro[6])
        self.txt_municipio.setText(campos_cadastro[7])
        self.txt_estado.setText(campos_cadastro[8])
        
    def new_record_comp(self):
        connect = data_base()

        fulldataset=(
            self.txt_cnpj.text(),self.txt_dtabertura.text(),self.txt_nomempresa.text(),self.txt_situacao.text(),self.txt_logradouro.text(),self.txt_numeroemp.text(),
            self.txt_complemento.text(),self.txt_municipio.text(),self.txt_estado.text(),self.txt_porte.text(),self.txt_tipo_cadastro.currentText(),
            datetime.datetime.now().strftime('%m-%d-%Y %H:%M'),"userr"
        )

        campos = ('cnpj', 'abertura', 'nome', 'situacao', 'logradouro', 'numero', 'complemento', 'municipio', 'uf', 'porte', 'tipo_cadastro', 'registro_db', 'user')     
        query = (
            f"""INSERT INTO empresas {campos}
            VALUES {fulldataset};"""
        )


        connect.executa_DML(query)    
        
    def update_data(self):
        connect = data_base()
        query = (
            f"""UPDATE empresas
            SET {coluna} = {valor}
            WHERE {id_number}"""
            )

    def buscar_dados(self):
        connect=data_base()
        resultado = connect.executa_DQL("SELECT * FROM empresas")
        
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(len(resultado))

        for row, text in enumerate(resultado):
            for column, data, in enumerate(text):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(data)))

        
        
        

if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
