from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from estoque_mp import carregar_estoque_mp, entrada_mp

app = FastAPI()

# Se quiser servir o HTML depois, descomente:
# app.mount("/", StaticFiles(directory="static", html=True), name="static")


@app.get("/")
def home():
    return {"status": "API OK"}


@app.get("/teste")
def teste():
    return {"mensagem": "Rota teste funcionando"}


@app.get("/api/mp/estoque")
def mp_estoque():
    itens = carregar_estoque_mp()
    return {"itens": itens}


@app.post("/api/mp/entrada")
def mp_entrada(dados: dict):
    try:
        entrada_mp(
            dados["cod"],
            dados["nome"],
            dados["quantidade"],
            dados["embalagem"],
            dados["empresa"]
        )
        return {"status": "sucesso", "mensagem": "Entrada registrada via API"}
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Campo faltando: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
