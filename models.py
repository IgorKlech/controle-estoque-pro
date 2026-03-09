from pydantic import BaseModel
from typing import Optional


class EntradaMP(BaseModel):
    ordem_compra: str
    cod_produto: str
    nome_produto: str
    quantidade: int  # FastAPI vai validar que é inteiro > 0
    embalagem: str
    empresa: str


class SaidaMP(BaseModel):
    ordem_fabricacao: str
    cod_produto: str
    quantidade: int


class EntradaPA(BaseModel):
    nome: str
    quantidade: int
    peso: float
    embalagem: str
    ordem_fabricacao: str


class SaidaPA(BaseModel):
    nome: str
    quantidade: int
    peso: float
    embalagem: str
    numero_pedido: str
