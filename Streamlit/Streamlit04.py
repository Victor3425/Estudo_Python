import streamlit as st
import pandas as pd
import numpy as np

#Textos
st.header('Minha dashboard')
st.sidebar.header('Escolha o que deseja filtrar')

if st.sidebar.button('Exbir gráficos'):
    # Exibição de dados
    df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['Preço', 'Taxa de ocupação','Taxa de inadimplência']
)
    
check = st.sidebar.checkbox('Aceitos')

if check:
    st.write('Marcado')



opcao = st.radio(
    'Selecione uma opção',
    ('Opção 1','Opção 2')
)

if opcao == 'Opção 1':
    st.heard('Selecionei a opção 1')
elif opcao == 'Opção 2':
        st.heard('Selecionei a opção 2')