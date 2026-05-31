import streamlit as st

st.title("🥩 Calculadora de Proteína, Carboidrato e Água")

nome = st.text_input("Informe seu nome")
peso = st.number_input("Digite seu peso (kg)", min_value=1.0)
refeicoes = st.number_input("Quantas refeições você faz por dia?", min_value=1, step=1)

if st.button("Calcular"):
    proteina_total = peso * 2
    carboidrato_total = peso * 3
    agua = peso * 33

    proteina_refeicao = proteina_total / refeicoes
    carboidrato_refeicao = carboidrato_total / refeicoes

    st.success(f"Olá, {nome}!")

    st.subheader("Necessidades diárias")
    st.write(f"**Proteína:** {proteina_total:.1f} g")
    st.write(f"**Carboidrato:** {carboidrato_total:.1f} g")
    st.write(f"**Água:** {agua:.0f} mL")

    st.subheader(f"Dividindo em {refeicoes} refeições")
    st.write(f"**Proteína por refeição:** {proteina_refeicao:.1f} g")
    st.write(f"**Carboidrato por refeição:** {carboidrato_refeicao:.1f} g")
