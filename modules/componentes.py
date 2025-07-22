import streamlit as st
from typing import Dict, List


def render_questionario(itens_por_bloco: Dict[str, List[str]]) -> dict | None:
    """
    Renderiza os itens do questionário com sliders organizados por bloco, respeitando rótulos distintos.

    Args:
        itens_por_bloco (dict): Dicionário com os nomes dos blocos como chave e listas de itens como valor.

    Returns:
        dict | None: Dicionário com as respostas se o formulário for enviado corretamente; caso contrário, None.
    """
    with st.form(key="form_questionario"):

        respostas_usuario = {}
        contador = 1  # numeração global dos itens

        for nome_bloco, itens in itens_por_bloco.items():
            st.markdown(f"### {nome_bloco}")

            if "LS/LLMs" in nome_bloco:
                label_min = "1 - Nunca"
                label_max = "7 - Sempre"
            else:
                label_min = "1 - Discordo totalmente"
                label_max = "7 - Concordo totalmente"

            for item in itens:
                st.slider(
                    label=f"{contador}. {item}",
                    min_value=1,
                    max_value=7,
                    value=4,
                    format="%d",
                    key=f"item_{contador}",
                    help=f"{label_min} — {label_max}"
                )

                respostas_usuario[f"item_{contador}"] = st.session_state[f"item_{contador}"]
                contador += 1
        placeholder = st.empty()
        enviado = st.form_submit_button("Enviar Respostas", use_container_width=True)

    if enviado:
        placeholder.success("✅ Respostas enviadas com sucesso!")
        return {"respostas": respostas_usuario}

    return None
