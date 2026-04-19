import streamlit as st
from agente import responder_usuario
from utils import calcular_gastos_mes, calcular_saldo_restante, ultimas_transacoes

st.set_page_config(page_title="Coink AI", page_icon="🐷", layout="wide")

st.title("🐷 Coink AI")
st.caption("Seu assistente inteligente de finanças pessoais")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total gasto no mês", f"R$ {calcular_gastos_mes():.2f}")

with col2:
    st.metric("Saldo restante", f"R$ {calcular_saldo_restante():.2f}")

st.subheader("Últimas transações")
st.dataframe(ultimas_transacoes(), use_container_width=True)

st.subheader("Chat com o Coink AI")
pergunta = st.text_input("Digite sua pergunta")

if st.button("Enviar") and pergunta:
    with st.spinner("Pensando..."):
        resposta = responder_usuario(pergunta)
    st.success(resposta)