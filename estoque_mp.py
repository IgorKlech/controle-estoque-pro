import json
from pathlib import Path

ARQUIVO_ESTOQUE_MP = Path("estoque_mp.json")

def carregar_estoque_mp() -> list:
    """Carrega o estoque de matéria-prima do JSON, ou devolve lista vazia."""
    if ARQUIVO_ESTOQUE_MP.is_file():
        with ARQUIVO_ESTOQUE_MP.open("r", encoding="utf-8") as f:
            return json.load(f)
    return []

def salvar_estoque_mp(estoque: list) -> None:
    """Salva o estoqye de matéria-prima no JSON"""
    with ARQUIVO_ESTOQUE_MP.open("w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=2, ensure_ascii=False)

def encontrar_item_por_cod(estoque: list, cod: str) -> dict | None:
    """Procura um item pelo código no estoque."""
    for item in estoque:
        if item["cod"] == cod:
            return item
    return None

def entrada_mp(cod: str, nome: str, quantidade: int, embalagem: str, empresa: str) -> None:
    """Registra etreada de matéria-prima (aumenta estoque)."""
    estoque = carregar_estoque_mp()
    item = encontrar_item_por_cod(estoque, cod)

    if item is None:
        # Cria novo item
        item = {
            "cod": cod,
            "nome": nome,
            "estoque": 0,
            "embalagem": embalagem,
            "empresa": empresa
        }
        estoque.append(item)

    item["estoque"] += quantidade

    salvar_estoque_mp(estoque)
    print(f"✅ Entrada registrada: {quantidade} un de {nome} (cod {cod}). Estoque atual: {item['estoque']}")

def saida_mp(cod: str, quantidade: int) -> None:
    """Registar saída de matéria-prima (diminui estoque)."""
    estoque = carregar_estoque_mp()
    item = encontrar_item_por_cod(estoque, cod)

    if item is None:
           print(f"❌ Código {cod} não encontrado no estoque.")
           return

    if quantidade > item["estoque"]:
        print(f"❌ Estoque insuficiente. Atual: {item['estoque']}, solicitado: {quantidade}")
        return
    
    item["estoque"] -= quantidade
    salvar_estoque_mp(estoque)
    print(f"✅ Saída registrada: {quantidade} un de {item['nome']} (cod {cod}). Estoque atual: {item['estoque']}")

def listar_estoque_mp() -> None:
    """Mostra o estoque atual de matéria-prima."""
    estoque = carregar_estoque_mp()
    if not estoque:
        print("⚠️ Estoque de matéria-prima vazio.")
        return
    print("\n📦 Estoque de Matéria-Prima:")
    print("-" * 50)
    for item in estoque:
        print(f"{item['cod']} - {item['nome']} | Estoque: {item['estoque']} | Emb: {item['embalagem']} | Emp: {item['empresa']}")
    print("-" * 50)