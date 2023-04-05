# FUNÇÃO ANTIGA

prod = conexao.query(f"SELECT * FROM produtos")
print(f"{'Lista de produtos': ^24}\n")
print(f"{'Id': ^5}{'PRODUTO': ^11}{'PREÇO': ^10}\n------------------------")
for id, nome, preco in prod:
			preco = "{:.2f}".format(preco)
	print(f"{f'{id}': ^4}|{f'{nome}': ^11}| R${preco}")
print()

# FUNÇÃO ATUALIZADA

ultimo_id = conexao.query("SELECT max(id) FROM produtos") # PEGA O ULTIMO ID DE PRODUTOS

print(f"{'Id': ^5}{'PRODUTO': ^11}{'PREÇO': ^10}\n------------------------")

for i in range(1, ultimo_id + 1): # PROCURANDO ID POR ID EM PRODUTOS
	try: # TENTA FAZER ISSO, SE NAO DER DAI ELE PASSA O ID INEXISTENTE!
		prod = conexao.query(f"SELECT id, nome, preco FROM produtos WHERE id = {i}") # AQUI ELE PEGA OS ELEMENTOS AONDE O ID FOR O INDICE i DO PRIMEIRO FOR
		for id, nome, preco in prod: # AQUI ELE PRINTA
			preco = "{:.2f}".format(preco)
			print(f"{f'{id}': ^4}|{f'{nome}': ^11}| R${preco}")
	except:
		pass
