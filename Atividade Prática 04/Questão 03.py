while True:
    try:
        senha = input("Digite a senha: ")

        if senha.lower() == 'sair':
            print("Saindo do programa...")
            break

        if len(senha) < 8:
            raise Exception("A Senha deve ter pelo menos 8 caracteres")

        tem_numero = False
        for caractere in senha:
    
        if tem_numero == False:
            raise Exception("A Senha deve conter pelo menos um número")
        
        print("Senha Válida")
               
    except Exception as e:
        print(f"Erro: {e} Tente novamente.")