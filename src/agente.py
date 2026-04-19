import json
import requests
from config import OLLAMA_MODEL, OLLAMA_URL
from utils import (
    carregar_resumo_usuario,
    carregar_orcamento,
    calcular_gastos_mes,
    calcular_saldo_restante,
    ultimas_transacoes,
)

SYSTEM_PROMPT = """
Você é o Coink AI, um assistente virtual especializado em finanças pessoais.
Seu objetivo é ajudar o usuário a controlar gastos, consultar despesas,
acompanhar orçamento mensal e responder de forma clara, amigável e objetiva.

Regras:
- Baseie-se apenas nos dados fornecidos.
- Nunca invente valores ou transações.
- Use sempre Real brasileiro (R$).
- Se faltar contexto, informe isso com transparência.
- Não faça recomendações de investimento avançadas.
"""


def montar_contexto():
    usuario = carregar_resumo_usuario()
    orcamento = carregar_orcamento()
    total_gasto = calcular_gastos_mes()
    saldo_restante = calcular_saldo_restante()
    transacoes = ultimas_transacoes().to_dict(orient="records")

    contexto = {
        "usuario": usuario,
        "orcamento": orcamento,
        "total_gasto_mes": total_gasto,
        "saldo_restante": saldo_restante,
        "ultimas_transacoes": transacoes,
    }
    return json.dumps(contexto, ensure_ascii=False, indent=2)


def responder_usuario(pergunta: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

Contexto financeiro do usuário:
{montar_contexto()}

Pergunta do usuário:
{pergunta}
"""

    payload = {
        "model": OLLAMA_MODEL,
        "prompt": prompt,
        "stream": False,
    }

    resposta = requests.post(OLLAMA_URL, json=payload, timeout=60)
    resposta.raise_for_status()
    return resposta.json()["response"]