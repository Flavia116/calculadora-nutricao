import streamlit as st

st.title("🏋️ Calculadora de Necessidades Diárias")

nome = st.text_input("Informe seu nome").upper()
peso = st.number_input("Peso (kg)", min_value=1.0)
altura = st.number_input("Altura (m)", min_value=0.50, format="%.2f")
refeicoes = st.number_input("Número de refeições", min_value=1, step=1)

if st.button("Calcular"):

    imc = peso / (altura * altura)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
        proteina = peso * 1.8
        carboidrato = peso * 4

    elif imc < 25:
        classificacao = "Peso ideal"
        proteina = peso * 1.8
        carboidrato = peso * 3

    elif imc < 30:
        classificacao = "Sobrepeso"
        proteina = peso * 2
        carboidrato = peso * 2

    elif imc < 35:
        classificacao = "Obesidade Grau I"
        proteina = peso * 1.4
        carboidrato = peso * 2

    elif imc < 40:
        classificacao = "Obesidade Grau II"
        proteina = peso * 1.4
        carboidrato = peso * 1.6

    else:
        classificacao = "Obesidade Grau III"
        proteina = peso * 1.4
        carboidrato = peso * 1.5

    agua = peso * 35

    proteina_refeicao = proteina / refeicoes
    carboidrato_refeicao = carboidrato / refeicoes

    st.success(f"Olá, {nome}!")

    st.subheader("Resultado")

    st.write(f"**IMC:** {imc:.1f}")
    st.write(f"**Classificação:** {classificacao}")

    st.subheader("Necessidades diárias")

    st.write(f"🥩 Proteína: **{proteina:.1f} g**")
    st.write(f"🍚 Carboidrato: **{carboidrato:.1f} g**")
    st.write(f"💧 Água: **{agua:.0f} mL**")

    st.subheader(f"Distribuição em {refeicoes} refeições")

    st.write(f"🥩 Proteína por refeição: **{proteina_refeicao:.1f} g**")
    st.write(f"🍚 Carboidrato por refeição: **{carboidrato_refeicao:.1f} g**")
