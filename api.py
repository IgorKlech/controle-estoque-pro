from fastapi import FastAPI, HTTPException
from estoque_mp import carregar_estoque_mp, entrada_mp, saida_mp
from estoque_pa import carregar_estoque_pa

app = FastAPI(title="Controle de Estoque - API v0.1")


@app.get("/")
async def raiz():
    return {"status": "ok", "mensagem": "API de Controle de Estoque rodando"}


@app.get("/api/mp/estoque")
async def api_listar_mp():
    """Lista o estoque de matéria-prima."""
    estoque = carregar_estoque_mp()
    return {"itens": estoque, "total": len(estoque)}


@app.post("/api/mp/entrada")
async def api_mp_entrada(
    cod: str,
    nome: str,
    quantidade: int,
    embalagem: str,
    empresa: str,
):
    """Endpoint simples para registrar entrada de MP via query/body."""
    if quantidade <= 0:
        raise HTTPException(status_code=400, detail="Quantidade deve ser > 0")

    # Reaproveita lógica do módulo
    entrada_mp(cod, nome, quantidade, embalagem, empresa)
    return {"status": "sucesso", "mensagem": "Entrada registrada"}


@app.post("/api/mp/saida")
async def api_mp_saida(
    cod: str,
    quantidade: int,
):
    """Endpoint simples para saída de MP."""
    if quantidade <= 0:
        raise HTTPException(status_code=400, detail="Quantidade deve ser > 0")

    saida_mp(cod, quantidade)
    return {"status": "sucesso", "mensagem": "Saída registrada"}


@app.get("/api/pa/estoque")
async def api_listar_pa():
    """Lista o estoque de produto acabado."""
    estoque = carregar_estoque_pa()
    return {"itens": estoque, "total": len(estoque)}
