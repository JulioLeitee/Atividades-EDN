'''1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente.
'''
import random
import string
def gerar_senha(tamanho_senha):
    caracteres = string.ascii_letters + string.digits + "@#$%&*()*,.!?;"
    senha = ''
    for i in range(tamanho_senha):
        senha += random.choice(caracteres)
    return senha


tamanho = int(input("Digite o tamanho da senha: "))
senha = gerar_senha(tamanho)
print("Senha gerada:", {senha})
      
