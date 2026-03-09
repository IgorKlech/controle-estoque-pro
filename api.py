from fastapi import FastAPI, HTTPException
from estoque_mp import carregar_estoque_mp, entrada_mp, saida_mp
from estoque_pa import carregar_estoque_pa
from models import EntradaMP, SaidaMP, EntradaPA, SaidaPA 

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
async def api_mp_entrada(entrada: EntradaMP):
    """Registra entrada de MP com validação Pydantic."""
    if entrada.quantidade <= 0:
        raise HTTPException(status_code=400, detail="Quantidade deve ser maior que 0")

    # Reaproveita a lógica existente
    entrada_mp(
        entrada.cod_produto,
        entrada.nome_produto,
        entrada.quantidade,
        entrada.embalagem,
        entrada.empresa
    )
    return {
        "status": "sucesso",
        "mensagem": f"Entrada registrada: {entrada.quantidade} un de {entrada.nome_produto}"
    }

@app.post("/api/mp/saida")
async def api_mp_saida(saida: SaidaMP):
    """Registra saída de MP com validação."""
    if saida.quantidade <= 0:
        raise HTTPException(status_code=400, detail="Quantidade deve ser maior que 0")

    saida_mp(saida.cod_produto, saida.quantidade)
    return {"status": "sucesso", "mensagem": "Saída registrada"}


@app.get("/api/pa/estoque")
async def api_listar_pa():
    """Lista o estoque de produto acabado."""
    estoque = carregar_estoque_pa()
    return {"itens": estoque, "total": len(estoque)}
