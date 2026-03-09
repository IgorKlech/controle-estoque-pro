import json

# Lista de produtos (estoque real)
estoque = [
    {"cod": "ACO-001", "nome": "Aço carbono", "estoque": 250},
    {"cod": "PLA-002", "nome": "Plástico ABS", "estoque": 120},
    {"cod": "PAR-M6", "nome": "Parafuso M6", "estoque": 500}
]

# Salvar
with open("estoque_completo.json", "w") as f:
    json.dump(estoque, f, indent=2)

print("✅ Estoque completo salvo!")
