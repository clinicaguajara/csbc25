import streamlit as st
from questionario.itens import ABM_4, LS_LLMs_6, TAME_LLMs_5
from modules.componentes import render_questionario

# Configuração da página
st.set_page_config(page_title="CSBC25", layout="centered")

st.title("📋 Hora da Dinâmica!")

# Define os blocos
BLOCOS = {
    "ABM-4": ABM_4,
    "LS/LLMs-6": LS_LLMs_6,
    "TAME/LLMs-5": TAME_LLMs_5,
}

# Renderiza formulário
payload = render_questionario(BLOCOS)

# Função de cálculo de percentil
def calc_percentil(valor, media, dp):
    from scipy.stats import norm
    z = (valor - media) / dp
    return round(norm.cdf(z) * 100, 1)

if payload:

    st.subheader("Seus resultados comparados com o grupo de validação")
    st.caption("Referência: 178 estudantes de graduação do Centro de Informática da UFPB")

    respostas_numericas = list(payload["respostas"].values())

    # Resgate por blocos
    abm_4 = respostas_numericas[0:4]
    ls_llms_6 = respostas_numericas[4:10]
    tame_5 = respostas_numericas[10:15]

    # === CÁLCULO ABM-4 ===
    escore_abm = sum(abm_4)
    percentil_abm = calc_percentil(escore_abm, 17.58, 5.05)

    # === CÁLCULO LS/LLMs-6 ===
    mls = ls_llms_6[0] + ls_llms_6[1] + ls_llms_6[2]  # Itens metacognitivos
    dls = ls_llms_6[3] + ls_llms_6[4] + ls_llms_6[5]  # Itens disfuncionais
    escore_ls = mls - dls
    percentil_ls = calc_percentil(escore_ls, 2.43, 5.28)
    percentil_mls = calc_percentil(mls, 13.79, 4.51)
    percentil_dls = calc_percentil(dls, 11.37, 3.56)

    # === CÁLCULO TAME/LLMs-5 ===
    item_reverso = 8 - tame_5[4]
    tame_corrigido = sum(tame_5[:4]) + item_reverso
    percentil_tame = calc_percentil(tame_corrigido, 22.89, 5.16)

    # === APRESENTAÇÃO DOS RESULTADOS ===
    st.markdown("#### Burnout Acadêmico (ABM-4)")
    st.caption("Academic Burnout Model (4 items)")
    st.write(f"• Sua pontuação: `{escore_abm}`")
    st.write("• Média: 17.58 | DP: 5.05")
    st.write(f"• **Percentil:** {percentil_abm}")

    st.markdown("#### Estratégias de Aprendizagem com LLMs (LS/LLMs-6)")
    st.caption("Learning Strategies Scale with LLMs (6 items)")
    st.write(f"• MLS (Metacognitivas): `{mls}` → **Percentil:** {percentil_mls}")
    st.write(f"• DLS (Disfuncionais): `{dls}` → **Percentil:** {percentil_dls}")
    st.write(f"• Índice Geral (LS/LLMs): `{escore_ls}`")
    st.write("• Média: 2.43 | DP: 5.28")
    st.write(f"• **Percentil**: {percentil_ls}")

    st.markdown("#### Confiança e Aceitação dos LLMs (TAME/LLMs-5)")
    st.caption("Technology Acceptance Model Edited to Assess LLMs Adoption (5 items)")
    st.write(f"• Sua pontuação: `{tame_corrigido}`")
    st.write("• Média: 22.89 | DP: 5.16")
    st.write(f"• **Percentil:** {percentil_tame}")
    st.divider()
    st.write("**Importante:** percentis não medem “acerto”, mas posição relativa. Eles são úteis para comparar seu resultado com um grupo normativo, como estudantes da mesma área ou idade.")
    st.caption("Um percentil 99 significa que você está no 1\% mais alto.")            
    st.caption("Um percentil 50 indica um desempenho mediano, igual à maioria.")
    st.caption("Um percentil 20 significa que 80\% das pessoas ficaram acima da sua pontuação.")

    st.markdown("Veja o [artigo referente à apresentação](https://www.researchgate.net/publication/393851562_How_Metacognition_Shapes_Higher_Education_Adoption_of_LLMs_A_Structural_Equation_Modeling_Approach)")
    st.markdown("E aqui o [artigo de validação das escalas](https://www.researchgate.net/publication/376859964_Assessing_the_Psychological_Impact_of_Generative_AI_on_Computer_and_Data_Science_Education_An_Exploratory_Study)")
    st.markdown("Conheça o meu trabalho no [instagram](https://www.instagram.com/clinicaguajara/)")
    st.write("Pela atenção, obrigado!!!")