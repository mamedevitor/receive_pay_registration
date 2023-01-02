from asyncio.streams import _ClientConnectedCallback
from datetime import datetime
import sql_query
import datetime

cliente = input("Nome do cliente:\n")
valor_recebido = input("Valor recebido:\n")
dta_recebimento = input("Data do recebiment:\n")
dta_registro = datetime.now().strftime('%m-%d-%Y %H:%M')
user = "usuario1"

fulldataset = (cliente, valor_recebido, dta_recebimento, dta_registro, user)
qtd = ("?, ?, ?, ?, ?")
query = "INSERT INTO recebimentos( cliente, valor_recebido, dta_recebimento, dta_registro, user) VALUES("+qtd+"),"+fulldataset