import streamlit as st
from translate import Translator
import requests 

base_url = 'https://api.github.com'
traduzir = Translator(from_lang="pt-br",to_lang="en")

def selecionar_usuario(username):
    url = f'{base_url}/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return None
    

def ui():
    st.markdown('''<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">''',unsafe_allow_html=True)
    st.title('Consulta Github')
    username = st.text_input('Insira o username de usuário do Github')

    if st.button('Buscar'):
        infoUsuario = selecionar_usuario(username)
        if infoUsuario is not None:
            st.markdown(f'''
            <div class="card" style="width: 18rem;">
            <img src="{infoUsuario['avatar_url']}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{infoUsuario['login']}</h5>
                <p class="card-text">{infoUsuario['bio']}</p>
                <a href="{infoUsuario['html_url']}"style="color: white" class="btn btn-primary">Ver perfil</a>
            </div>
            </div>    
                        ''',unsafe_allow_html=True)


ui()  