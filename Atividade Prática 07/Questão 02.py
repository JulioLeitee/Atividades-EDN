import csv

def escrever_csv(nome_arquivo, dados):
    try:
        with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
            escritor = csv.writer(arquivo_csv)
            escritor.writerows(['nome', 'idade', 'cidade'])
            for linha in dados:
                escritor.writerow(linha)
            return f"Dados escritos com sucesso em {nome_arquivo}"
    


    except Exeption as e:
        return f"Erro ao escrever no arquivo: {e}"


dados = [
    ['Julio', 28, 'Maceió'],
    ['Keyla', 12, 'Paraná'],
    ['Puskas', 35, 'Natal']
]

nome_arquivo = input("Digite o nome do arquivo CSV: ")
print (escrever_csv(nome_arquivo, dados))
