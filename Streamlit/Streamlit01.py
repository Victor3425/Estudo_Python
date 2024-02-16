import streamlit as st
import pandas as pd

st.set_page_config(page_title='Meu site Streamlit')


with st.container():
    st.subheader('Meu primeiro site com Streamlit')
    st.title('Dashboard de Contratos')
    st.write('Inforções sobre os contratos fechados pela CAOA ao longo do mês de Maio ')
    st.write('Quer aprender Python? [Clique aqui](https://pypi.org/project/streamlit/)')

@st.cache_data
def carregar_dados():
    tabela = pd.read_csv(r'C:\Users\victor.rodriguess\Documents\EstudoPython\resultados.csv')
    return tabela


with st.container():
    st.write('---')
    qtde_dias = st.selectbox('Selecione o período',['7D','15D','21D','30D'])
    num_dias = int(qtde_dias.replace('D',''))
    dados = carregar_dados()
    dados = dados[-num_dias:]
    st.area_chart(dados, x='Data', y='Contratos')




