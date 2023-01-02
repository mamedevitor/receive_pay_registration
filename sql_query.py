# Bibliotecas utilizadas
import sqlite3

class data_base():
    def __init__(self):
        self.db = "receive_pay_registration.db"

    def conecta(self):
        self.con= sqlite3.connect(self.db)
        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()

    # Select
    def executa_DQL(self,sql):
        self.conecta()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.desconecta
        return res

    #Insert, update, delete
    def executa_DML(self, sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit()
        self.desconecta
    


if __name__ == "__main__":
    connection = data_base()
    connection.conecta()
    ret= connection.executa_DQL("SELECT * FROM empresas")
    print(ret)
    # execute_querys(
    #     "CREATE",
    #     """CREATE TABLE IF NOT EXISTS users(
    #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    #         user TEXT NOT NULL, password TEXT NOT NULL, 
    #         access NOT NULL, registro_db TIMEVALUE NOT NULL);""",
    #         connection)
    # execute_querys(
    #     "CREATE",
    #     """CREATE TABLE IF NOT EXISTS empresas(
    #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
    #         cnpj TEXT NOT NULL,  
    #         abertura DATE NOT NULL,  
    #         nome TEXT NOT NULL,  
    #         situacao TEXT NOT NULL,  
    #         logradouro TEXT NOT NULL,  
    #         numero TEXT NOT NULL,  
    #         complemento TEXT NOT NULL,  
    #         municipio TEXT NOT NULL, 
    #         uf TEXT NOT NULL,  
    #         porte TEXT NOT NULL, 
    #         tipo_cadastro TEXT NOT NULL,
    #         registro_db TIMEVALUE NOT NULL, 
    #         user TEXT NOT NULL);""",
    #         connection)
    # execute_querys("CREATE",
    #     """CREATE TABLE IF NOT EXISTS recebimentos(
    #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #         cliente TEXT NOT NULL,
    #         valor_recebido NOT NULL,
    #         dta_recebimento DATE NOT NULL,
    #         data_registro TEMEVALUE NOT NULL,
    #         user TEXT NOT NULL);""",
    #         connection) 
    # execute_querys("CREATE",
    #     """CREATE TABLE IF NOT EXISTS pagamentos(
    #         id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    #         fornecedor TEXT NOT NULL, 
    #         valor_recebido NOT NULL, 
    #         dta_pagamento DATE NOT NULL, 
    #         data_registro DATETIME NOT NULL, 
    #         usuario TEXT NOT NULL)""",
    #         connection)