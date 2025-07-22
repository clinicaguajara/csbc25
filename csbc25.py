import streamlit as st
from questionario.itens import ABM_4, LS_LLMs_6, TAME_LLMs_5
from modules.componentes import render_questionario

st.set_page_config(page_title="CSBC25", layout="centered")
st.title("📋 Questionário")

# Define os blocos com nomes legíveis
BLOCOS = {
    "ABM-4": ABM_4,
    "LS/LLMs-6": LS_LLMs_6,
    "TAME/LLMs-5": TAME_LLMs_5,
}

# Renderiza o formulário
payload = render_questionario(BLOCOS)

if payload:
    st.success("✅ Respostas enviadas com sucesso!")

    st.subheader("📊 Seus resultados comparados com o grupo de validação")
    st.caption("Referência: 178 estudantes de graduação do Centro de Informática da UFPB")

    # As respostas já são inteiros (1 a 7)
    respostas_numericas = list(payload["respostas"].values())

    # Separação por blocos
    abm_4 = respostas_numericas[0:4]
    ls_llms_6 = respostas_numericas[4:10]
    tame_5 = respostas_numericas[10:15]

    # Cálculos das escalas
    MLS_LLMs_3 = ls_llms_6[1] + ls_llms_6[2] + ls_llms_6[4]
    TAME_5 = sum(tame_5)
    LS_LLMs_6 = sum(ls_llms_6[:3]) - sum(ls_llms_6[3:])

    def calc_percentil(valor, media, dp):
        from scipy.stats import norm
        z = (valor - media) / dp
        return round(norm.cdf(z) * 100, 1)

    # Apresentação dos resultados
    st.markdown("**Escala MLS/LLMs-3**")
    st.write(f"• Sua pontuação: `{MLS_LLMs_3}`")
    st.write("• Média: 13.79 | DP: 4.51")
    st.write(f"• Percentil: {calc_percentil(MLS_LLMs_3, 13.79, 4.51)}")

    st.markdown("**Escala TAME/LLMs-5**")
    st.write(f"• Sua pontuação: `{TAME_5}`")
    st.write("• Média: 22.89 | DP: 5.16")
    st.write(f"• Percentil: {calc_percentil(TAME_5, 22.89, 5.16)}")

    st.markdown("**Escala LS/LLMs-6**")
    st.write(f"• Sua pontuação: `{LS_LLMs_6}`")
    st.write("• Média: 2.43 | DP: 5.28")
    st.write(f"• Percentil: {calc_percentil(LS_LLMs_6, 2.43, 5.28)}")
