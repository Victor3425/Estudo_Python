import streamlit as st
import pandas as pd
import openai



st.title('Dashboard Atendimento ao Cliente')

data = open(r'C:\Users\victor.rodriguess\Documents\EstudoPython\Call Center Data.csv')
df = pd.read_csv(data)


# Convertendo colunas
df['Answer Rate'] = df['Answer Rate'].str.rstrip('%').astype(float)/100

# Criando Metricas
incomeng_avg = df['Incoming Calls'].mean()
answered_avg = df['Answered Calls'].mean()
ans_rate_avg = df['Answer Rate'].mean()

col1,col2,col3 = st.columns(3)
col1.metric('Incoming Calls AVG',round(incomeng_avg))
col2.metric('Answered Calls AVG',round(answered_avg))
col3.metric('Answered Rate',round(ans_rate_avg *100,1))

st.line_chart(df[['Incoming Calls','Answered Calls']])

openai.api_key = ''

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content": f"O dataset a seguir corresponde a metricas de negócio de uma operação de suporte. Me informe 5 insights sobre este dataset {df}"}
    ]
)

st.markdown(completion['choices'][0]['message']['content'])
