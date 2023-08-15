import os
import json

def extract_route(requisicao):

    comeco = requisicao.find("/") + 1
    rota = requisicao[comeco:]
    fim = rota.find(" ")
    return rota[:fim]

def read_file(path):

    with open(path, "rb") as f:
        return f.read()
    
def load_data(nome):

    with open(f"./data/{nome}") as f:
        data = json.load(f)

    return data

def load_template(arquivo):

    with open(f"templates/{arquivo}") as f:
        return f.read()