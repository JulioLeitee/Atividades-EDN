nome_produto = input("Digite o nome do produto: ")
valor = float(input("Digite o preço unitário do produto: "))
desconto = 20 

valor_desconto = valor * (desconto / 100)
valor_final = valor - valor_desconto

print(f"Produto: {nome_produto}")
print(f"preço unitário: R$ {valor:.2f}")
print(f"Desconto: {desconto}%")
print(f"preço total: R$ {valor_final:.2f}")