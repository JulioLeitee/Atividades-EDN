''' Crie um programa que consulte informações de um CEP na API ViaCEP, retorne logradouro, bairro, cidade e estado do CEP digitado, 
caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.'''

import requests
def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if 'erro' in dados:
            return "CEP Inválido"
    
        logradouro = dados['logradouro']
        bairro = dados['bairro']
        cidade = dados['localidade']
        uf = dados['uf']

        return f'Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {uf}'
    except requests.RequestException as e:
        return f"Erro ao consultar CEP: {e}"
    
cep = input("Digite o CEP: ")
resultado = consultar_cep(cep)  
print(resultado)

