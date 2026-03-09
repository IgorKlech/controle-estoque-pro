import json

produto = {
    "nome": "Parafuso M6",
    "cod" : "PAR-M6",
    "estoque" : 500
}

with open("protudos.json","w") as arquivo:
    json.dump(produto, arquivo, indent=2)

print("✅ Produto salvo!")

with open("produto.json", "r") as arquivo:
    produto_lido = json.load(arquivo)

print("Produto lido:", produto_lido["nome"])
print("Estoque atual:", produto_lido["estoque"])