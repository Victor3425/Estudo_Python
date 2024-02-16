import fitz  # PyMuPDF
import pandas as pd


def ler_pdf(caminho_arquivo):
    texto = ''
    documento = fitz.open(caminho_arquivo)

    for pagina_num in range(documento.page_count):
        pagina = documento.load_page(pagina_num)
        texto += pagina.get_text()

    documento.close()
    return texto

# Substitua 'seu_arquivo.pdf' pelo caminho do seu arquivo PDF
caminho_do_arquivo = 'Hyundai - 2023-12-06.pdf'
texto_do_pdf = ler_pdf(caminho_do_arquivo)

# Criar um DataFrame com uma coluna chamada 'Texto', onde cada linha do texto se torna uma entrada
df = pd.DataFrame({'Texto': texto_do_pdf.split('\n')})

# Imprimir DataFrame
print(df[5:6])

