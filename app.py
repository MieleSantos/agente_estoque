import streamlit as st

from agent import seach_agent, select_model

st.set_page_config(
    page_title='Estoque GPT',
    page_icon='📄',
)
st.header('Assistente de Estoque')


selected_model = st.sidebar.selectbox(
    label='Selecione o modelo LLM',
    options=select_model(),
)

st.sidebar.markdown('### Sobre')
st.sidebar.markdown(
    'Este agente consulta um banco de dados de estoque utilizando um modelo GPT.'
)

st.write('Faça perguntas sobre o estoque de produtos, preços e reposições.')
user_question = st.text_input('O que deseja saber sobre o estoque?')

if st.button('Consultar'):
    if user_question:
        with st.spinner('Consultando o banco de dados...'):
            response = seach_agent(user_question, selected_model)

            st.markdown(response.get('output'))
    else:
        st.warning('Por favor, insira uma pergunta.')
