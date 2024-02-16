import streamlit as st
import yfinance as yf
import datetime as dt

# Muda as configurações do site
st.set_page_config(page_title='Dashboard Financeiro',layout='wide')
st.title('Dashboard Financeiro')


end_date = dt.datetime.today()
start_date = dt.datetime(end_date.year -1,end_date.month,end_date.day)

with st.container():
    st.header('Insira as informações solicitadas abaixo:')

    col1, col2, col3 = st.columns(3)
    with col1:
        ativo = st.selectbox('Selecione o ativo desejado:', options=['PETR4.SA','VALE3.SA','MGLU3.SA','ITSA4.SA','TOTS3.SA'])
    with col2:
        data_inicial = st.date_input('Selecione a data Inicial:',start_date)
    with col3:
        data_final = st.date_input('Selecione a data Final:',end_date)



# Use a função Ticker para obter os dados
ticker = yf.Ticker(ativo)
df = ticker.history(start=data_inicial, end=data_final)

ult_atualizacao = df.index.max()
ult_cotacao = round( df.loc[df.index.max(),'Close'],2) # Ultima cotação encontrada
prim_cotacao = round( df.loc[df.index.min(),'Close'],2) # Ultima cotação encontrada
maior_cotacao = round(df['Close'].max(),2) # Maior cotação do perído
menor_cotacao = round(df['Close'].min(),2) # Menor cotação do perído
delta = round(((ult_cotacao-prim_cotacao)/prim_cotacao)*100,2)


with st.container():
    with col1:
        st.metric(f'Ultima atualização - {ult_atualizacao}','{:,.2f}'.format(ult_cotacao),f'{delta}%')
    with col2:
        st.metric('Menor cotação do periodo','{:,.2f}'.format(menor_cotacao))
    with col3:
        st.metric('Maior cotação do periodo','{:,.2f}'.format(maior_cotacao))


with st.container():
    st.area_chart(df[['Close']])
    st.line_chart(df[['Low','Close','High']])