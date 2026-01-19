
'''Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao, 
caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro. '''

import pandas as pd
def processar_logs_treinamento(arquivo_log):
    try:
        leitor = pd.read_csv(arquivo_log)
        media = leitor['tempo_execucao'].mean()
        desvio_padrao = leitor['tempo_execucao'].std()
        return f"Média: {media}, Desvio Padrão: {desvio_padrao}"
    

    except FileNotFoundError:
        return "Erro: Arquivo não encontrado."
    
    
arquivo = input("Digite o nome de log: ")
print(processar_logs_treinamento(arquivo))
