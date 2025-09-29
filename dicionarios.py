lista_produtos = ["airpod", "ipad", "iphone", "macbook"]
precos = [2000, 9000, 6000, 11000]

dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# pegar um elemento
#print(dic_produtos["ipad"])

# editar um elemento 
#dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
#print(dic_produtos)

# quantidade de itens do dicionário
#print(len(dic_produtos))

# retirar um item do dicionario
#dic_produtos.pop("airpod")
#print(dic_produtos)

# adicionar um item no dicionario
#dic_produtos["aplle watch"] = 2500
#print(dic_produtos)

#verificar se um item existe no dicionário
#if "iphone" in dic_produtos:
 #   print("Existe o produto")
#else:
  #  print("Não existe o produto")

#verificar se um valor existe nos valores do dicionario
#if 9000 in dic_produtos.values():
   # print("Existe")
#else:
 #   print("não existe")

# cadastrar o novo produto (se o produto não existir)
# caso o produto exista, ele vai editar o produto
nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do Produto:")

nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)
# além disso, o programa tem que atualizar o preço de todos os produtos para novos valores em 10% a mais do que o preço original
for produto in dic_produtos:
    novo_preco = dic_produtos[produto] * 1.1
    dic_produtos[produto] = novo_preco

print(dic_produtos)



