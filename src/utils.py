import json
import pandas as pd
from pathlib import Path

DATA_DIR = Path("data")


def carregar_transacoes():
    caminho = DATA_DIR / "transacoes.csv"
    return pd.read_csv(caminho)


def salvar_transacao(nova_transacao: dict):
    caminho = DATA_DIR / "transacoes.csv"
    df = pd.read_csv(caminho)
    df = pd.concat([df, pd.DataFrame([nova_transacao])], ignore_index=True)
    df.to_csv(caminho, index=False)


def carregar_orcamento():
    caminho = DATA_DIR / "orcamento_mensal.json"
    with open(caminho, "r", encoding="utf-8") as file:
        return json.load(file)


def carregar_resumo_usuario():
    caminho = DATA_DIR / "resumo_usuario.json"
    with open(caminho, "r", encoding="utf-8") as file:
        return json.load(file)


def calcular_gastos_mes():
    df = carregar_transacoes()
    despesas = df[df["tipo"].str.lower() == "despesa"]
    return float(despesas["valor"].sum())


def calcular_saldo_restante():
    orcamento = carregar_orcamento()
    total_gasto = calcular_gastos_mes()
    return float(orcamento["orcamento_total"]) - total_gasto


def ultimas_transacoes(limite=5):
    df = carregar_transacoes()
    return df.tail(limite)