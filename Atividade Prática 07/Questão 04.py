'''Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome, 
idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, 
caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.'''


import json

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_json:
            dados_json = json.load(arquivo_json)
            return dados_json
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não  encontrado")


def escrever_arquivo(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', encoding='utf-8') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4, ensure_ascii=False)
            return f"Dados escritos com sucesso no arquivo {nome_arquivo}"
    except FileNotFoundError:
        return f"Erro ao escrever no arquivo {e}"
    

dados = {
    "nome": "João",
    "idade": 25,
    "cidade": "São Paulo"}

nome = input("Digite o nome do arquivo JSON: ")
print(escrever_arquivo(nome, dados))
