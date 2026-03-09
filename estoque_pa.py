import json
from pathlib import Path
from collections import Counter

ARQUIVO_ESTOQUE_PA = Path("estoque_pa.json")


def carregar_estoque_pa() -> list:
    """Carrega o estoque de produto acabado do JSON, ou lista vazia se não existir/estiver vazio."""
    if ARQUIVO_ESTOQUE_PA.is_file():
        try:
            with ARQUIVO_ESTOQUE_PA.open("r", encoding="utf-8") as f:
                conteudo = f.read().strip()
                if not conteudo:
                    return []
                return json.loads(conteudo)
        except json.JSONDecodeError:
            return []
    return []


def salvar_estoque_pa(estoque: list) -> None:
    """Salva o estoque de produto acabado no JSON."""
    with ARQUIVO_ESTOQUE_PA.open("w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=2, ensure_ascii=False)


def encontrar_produto_por_nome(estoque: list, nome: str) -> dict | None:
    """Procura um produto acabado pelo nome."""
    for item in estoque:
        if item["nome"].lower() == nome.lower():
            return item
    return None


def entrada_pa(nome: str, quantidade: int, peso: float, embalagem: str, ordem_fabricacao: str) -> None:
    """Registra entrada de produto acabado (produção)."""
    estoque = carregar_estoque_pa()
    item = encontrar_produto_por_nome(estoque, nome)

    if item is None:
        item = {
            "nome": nome,
            "quantidade": 0,
            "peso_total": 0.0,
            "embalagem": embalagem,
            "ordem_ultima_fabricacao": ordem_fabricacao
        }
        estoque.append(item)

    item["quantidade"] += quantidade
    item["peso_total"] += peso
    item["ordem_ultima_fabricacao"] = ordem_fabricacao

    salvar_estoque_pa(estoque)
    print(f"✅ Entrada PA: {quantidade} un de {nome}. Qtd total: {item['quantidade']}, Peso total: {item['peso_total']:.2f} kg")


def saida_pa(nome: str, quantidade: int, peso: float, numero_pedido: str) -> None:
    """Registra saída de produto acabado (venda/expedição)."""
    estoque = carregar_estoque_pa()
    item = encontrar_produto_por_nome(estoque, nome)

    if item is None:
        print(f"❌ Produto {nome} não encontrado no estoque de PA.")
        return

    if quantidade > item["quantidade"]:
        print(f"❌ Estoque insuficiente. Atual: {item['quantidade']}, solicitado: {quantidade}")
        return

    item["quantidade"] -= quantidade
    item["peso_total"] -= peso  # simplificação, assume peso passado correto

    salvar_estoque_pa(estoque)
    print(f"✅ Saída PA: {quantidade} un de {nome} (Pedido {numero_pedido}). Qtd atual: {item['quantidade']}")


def listar_estoque_pa() -> None:
    """Mostra o estoque atual de produto acabado."""
    estoque = carregar_estoque_pa()
    if not estoque:
        print("⚠️ Estoque de produto acabado vazio.")
        return

    print("\n📦 Estoque de Produto Acabado:")
    print("-" * 60)
    for item in estoque:
        print(
            f"{item['nome']} | Qtd: {item['quantidade']} | "
            f"Peso total: {item['peso_total']:.2f} kg | Emb: {item['embalagem']}"
        )
    print("-" * 60)

def top_produtos_por_quantidade(top_n: int = 5) -> None:
    """Mostra os produtos mais presentes no estoque (por quantidade)."""
    estoque = carregar_estoque_pa()
    if not estoque:
        print("Sem dados para relatório de PA.")
        return

    # Ordena por quantidade desc
    ordenado = sorted(estoque, key=lambda item: item["quantidade"], reverse=True)

    print(f"\n🏆 Top {top_n} produtos por quantidade:")
    print("-" * 60)
    for item in ordenado[:top_n]:
        print(f"{item['nome']} | Qtd: {item['quantidade']} | Peso total: {item['peso_total']:.2f} kg")
    print("-" * 60)