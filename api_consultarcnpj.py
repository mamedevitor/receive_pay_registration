import requests
import json

def consultar_cnpj(cnpj):
    
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"
    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}
    response = requests.request("GET", url, params=querystring)
    
    resp = json.loads(response.text)
    
    return resp['cnpj'], resp ['abertura'], resp ['nome'], resp ['situacao'], resp ['logradouro'], resp ['numero'], resp ['complemento'], resp ['municipio'], resp ['uf'], resp ['porte']
    

consultar_cnpj('06990590000123')